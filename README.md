# SPARQL examples for PlantMetWiki: evidence tiers of pathway components

SPARQL queries, stored in the [SIB SPARQL examples](https://github.com/sib-swiss/sparql-examples/) format, that define the **evidence tiers** of the components of PlantMetWiki pathways (the reactions). They are used for scoring and prioritisation in the [lod-pathways](https://github.com/pathway-lod/lod-pathways-community) project.

## Queries

**Website:** <https://pathway-lod.github.io/sparql-examples-pmw/>, with a page per query: <https://pathway-lod.github.io/sparql-examples-pmw/examples/PlantMetWiki/>. The discussion of the tiers is in the [`minimum_information/`](https://github.com/pathway-lod/lod-pathways-community/tree/main/minimum_information) folder of lod-pathways-community.

| File | Tier | Target | Federates with |
|---|---|---|---|
| `examples/PlantMetWiki/00-reactions-per-tier.ttl` | overview: reactions and how many reach tiers 1 to 3 | PlantMetWiki | |
| `examples/PlantMetWiki/01-tier1-reaction-with-ec.ttl` | 1 `ec`: the reaction has an EC number | PlantMetWiki | |
| `examples/PlantMetWiki/02-tier2-reaction-matches-rhea.ttl` | 2 `rhea`: the Rhea identifier of the reaction is an approved reaction in Rhea | PlantMetWiki | Rhea |
| `examples/PlantMetWiki/03-tier3-reaction-with-reviewed-uniprot-enzyme.ttl` | 3 `uniprot`: the reaction names a UniProt enzyme, and whether it is reviewed | PlantMetWiki | UniProt |
| `examples/PlantMetWiki/04-tier4-pathway-enzyme-nodes-with-uniprot.ttl` | 4 `enzyme_node`: enzyme nodes with a UniProt ID per pathway, and how many are reviewed (4 example pathways) | PlantMetWiki | UniProt |
| `examples/PlantMetWiki/05-tier5-enzymes-with-orthologs-in-orthodb.ttl` | 5 `ortholog`: enzyme nodes whose UniProt entry is in an OrthoDB orthologous group (300 enzymes as an example; 620 group memberships in about 30 s) | PlantMetWiki | OrthoDB |
| `examples-local/01-claims-with-pathway-tiers.ttl` | the claims of the lod-pathways evidence graph with the tiers of their pathway | local graph | PlantMetWiki |

Results on the PlantMetWiki endpoint (release 17, 2026-11-10): of 7,772 reactions, 5,988 have an EC number, 1,193 a Rhea identifier and 1,062 a UniProt enzyme on the reaction itself. Queries 01 to 03 are limited to 100 rows as examples. The 5,547 UniProt-carrying enzyme nodes all have the xref source Uniprot-TrEMBL, so "reviewed" comes from UniProt.

**Not found yet:** enzyme nodes list the reactions they catalyse in a `Catalyzes` property (a comma-separated list of PlantCyc reaction IDs, for example `RXN-4FS-115`), but no reaction node of PlantMetWiki has such an ID as its `UniqueID`, in the pathways checked and in a query over the whole graph. A per-reaction enzyme tier therefore needs another route (for example the `EnzymaticReaction` property of the reactions, or the PlantCyc pathway files).

How PlantMetWiki stores this: the reactions are `gpml:Interaction` nodes with `v:gpmlProperty` key/value pairs (`EC_Number`, `AlternativeId_Rhea`, `AlternativeId_Uniprot`, `ReactionEquation`); the PlantCyc pathway number is in the IRI (`.../Pathway/PC800_r17.../Interaction/...`).

## Minimum information tiers

`examples/MinimumInformationTiers/` holds draft **minimum-information tiers for the results of the pilots**, one query per tier with a descriptive name (see [`minimum_information/`](https://github.com/pathway-lod/lod-pathways-community/tree/main/minimum_information) in lod-pathways-community). Each query carries a keyword per case of the project (a query that uses data of several cases has several) and a keyword for everything it uses, so the table of the folder page can be filtered by case or by resource.

The connectivity to PlantMetWiki (the metabolite, gene or pathway that a result matches) is **computed by the query** (first InChIKey block, Solyc locus, UniProt, Rhea), not read from stored anchor terms. These queries run on the evidence graphs of the pilots (`shape_constraints/rdf/` of lod-pathways-community) loaded into a local store, with PlantMetWiki, Rhea and UniProt called by `SERVICE`. Their `schema:target` is therefore a placeholder (`https://pathway-lod.github.io/sparql-examples-pmw/evidence-graph`) until the graphs are served from an endpoint. **Ranked megaqueries:** `ranked-pathway-metabolites`, `ranked-pathway-reactions` and `ranked-pathway-genes` combine the evidence of a scope as optional branches and add a `score` column. The evidence is grouped into **families of tiers that are not independent** (for example EC and Rhea; the annotation tools; for genes, the genes of a biosynthetic gene cluster together with the genes of a pathway); a component takes the weight of the strongest tier of each family, and `score = 1 - prod(1 - w_family)` (noisy-OR). The weights are drafts (see `minimum_information/notebooks/weights.csv` in lod-pathways-community); the notebook `05_ranked_components.ipynb` explores the results. The metabolite megaquery also contains the formula-layer proxy for structure similarity (capped at 3,000 rows) and the IDSM similarity to the substrates of one pathway (PC968), and takes about 10 minutes. The Rhea step between metabolites is not in the live megaqueries: asked through PlantMetWiki it exceeds the 60 s limit of the endpoint (tested with 30 reactions); its weights are in `weights.csv` for when it is materialised.

**Output of the queries:** each one returns a list of pathway components that reach the level of evidence, with the columns `component`, `componentType` (reaction, metabolite or gene), `pathway` (the putative or supported pathway) and the evidence as metadata (for example the number of supporting tools, features or associations, the scores, the gene or enzyme it is inferred from). Every query has keywords for what it uses (for example Rhea, co-expression, biosynthetic gene cluster, gene-metabolite association); the keyword *no data yet* marks queries written against the proposed data model that return no rows on the current graphs, and the comment of each query says how it was tested.

```bash
R=../lod-pathways-community
.venv/bin/python run_examples.py examples/MinimumInformationTiers --data $R/shape_constraints/rdf/annotation.ttl
```

## Run them

```bash
uv venv --python 3.12 .venv && uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/python run_examples.py                                   # endpoint queries (needs internet)
.venv/bin/python run_examples.py examples-local --data ../lod-pathways-community/examples/sample_evidence_graph.ttl
```

`run_examples.py` reads each Turtle file, runs the query on its `schema:target` and prints the number of rows. The GitHub workflow uses the Java tester of `sparql-examples-utils` (Java 17 or newer; not run locally) for the files of `examples/`.

## Querying the lod-pathways evidence graphs together with PlantMetWiki

The evidence graphs of lod-pathways (`examples/sample_evidence_graph.ttl` and the files of `shape_constraints/rdf/`) use the proposed terms (ECO evidence classes, the placeholder `lodp:` terms such as `lodp:anchorTier`, SIO, PROV). A public endpoint cannot read local files, so these queries run the other way round: **load the graph into a local store and call PlantMetWiki, Rhea and UniProt from it with `SERVICE`**. The files of `examples-local/` have the placeholder target `<https://pathway-lod.github.io/sparql-examples-pmw/evidence-graph>` and are not run by the workflow. To use the files of `shape_constraints/rdf/` (large) load them with `--data` in the same way. The longer-term alternative is to load the graphs into a triple store with a SPARQL endpoint of the project and give that endpoint as the target.

# Template notes (from the template repository)

# SPARQL examples template repository

This is a template repository to help you get started with sharing your sparql examples in a structured maner.


The idea comes from the [SIB SPARQL Examples](https://github.com/sib-swiss/sparql-examples/) project. 

# Upon forking

Change YOUR\_PROJECT to what you need it to be, adapt the index.md files.
Add your prefixes.ttl and examples in \*.ttl files.
Correct the LICSENSE.md and CITATION.cff to account for your project.


# For more inspiration see

 * [SIB Sparql Examples](https://github.com/sib-swiss/sparql-examples/)
 * [Wikibase Examples](https://github.com/JervenBolleman/wikibase-sparql-examples/)
 * [BiGCAT-UM](https://github.com/BiGCAT-UM/sparql-examples)

# The QA and markdown 

Can be found in the project [SIB SPARQL Examples Utils](https://github.com/sib-swiss/sparql-examples-utils/)

# How to test github page rendering locally

```sh
docker build -t sparql-examples-template .
docker run --rm -v "$PWD":/srv/jekyll sparql-examples-template bundler exec jekyll build --watch &
python3 -m http.server 8792 --directory _site
```
Build a local docker image that has the right Jekyll version and use that to build the webpages.
Then serve that with the python3 inbuild basic http server.
Open a browser locally at `http://localhost:8792/` to see the rendered HTML.

