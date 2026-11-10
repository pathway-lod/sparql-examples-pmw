#!/usr/bin/env python3
"""Run the SPARQL examples of this repository and print the number of rows.

  python run_examples.py [examples/PlantMetWiki]                        # queries on their schema:target endpoint
  python run_examples.py examples-local --data graph.ttl [graph2.ttl]   # queries on a LOCAL graph that may use SERVICE to endpoints

Requirements: requests, rdflib (reads the Turtle files; a syntax error shows up here) and pyoxigraph (the local store; it runs the
SERVICE clauses). A local example has the placeholder target <urn:lodp:local-graph>. This script is a stand-in for the Java tester
of the GitHub workflow (sparql-examples-utils, Java 17 or newer), which only knows endpoint queries.
"""
import sys
import time
from pathlib import Path

import pyoxigraph as ox
import requests
from rdflib import Graph, Namespace

SH, SCHEMA = Namespace("http://www.w3.org/ns/shacl#"), Namespace("https://schema.org/")
LOCAL = "urn:lodp:local-graph"

args = sys.argv[1:]
data = args[args.index("--data") + 1:] if "--data" in args else []
folder = Path(args[0] if args and args[0] != "--data" else "examples/PlantMetWiki")
store = ox.Store()
for f in data:
    store.load(path=f, format=ox.RdfFormat.TURTLE)
if data:
    print(f"local graph: {len(store)} triples from {len(data)} file(s)")


def show(name, rows, t0):
    print(f"{name}: {len(rows)} rows in {time.time() - t0:.0f} s")
    for b in rows[:6]:
        print("    ", {k: v[-60:] for k, v in b.items()})


for path in sorted(folder.glob("*.ttl")):
    if path.name == "prefixes.ttl":
        continue
    g = Graph().parse(path)
    for ex in g.subjects(SCHEMA.target, None):
        query = next((str(o) for p in (SH.select, SH.ask, SH.construct) for o in g.objects(ex, p)), None)
        target = str(next(g.objects(ex, SCHEMA.target)))
        t0 = time.time()
        if target == LOCAL:
            res = store.query(query)
            show(path.name, [{str(v.value): str(row[v].value) for v in res.variables if row[v] is not None} for row in res], t0)
            continue
        r = requests.post(target, data={"query": query}, headers={"Accept": "application/sparql-results+json"}, timeout=290)
        if r.status_code != 200:
            print(f"{path.name}: HTTP {r.status_code} {r.text[:200]!r}")
            continue
        show(path.name, [{k: v["value"] for k, v in b.items()} for b in r.json()["results"]["bindings"]], t0)
