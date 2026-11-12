# SPARQL examples

SPARQL queries for the PlantMetWiki knowledge graph that define evidence tiers. Each query is one Turtle file in the SIB SPARQL-examples format, with keywords for what it uses; many are federated with Rhea, UniProt and OrthoDB.

* [PlantMetWiki](./examples/PlantMetWiki/): evidence tiers of pathway components (EC number, Rhea, UniProt, enzyme nodes, orthologs)
* [Minimum information tiers](./examples/MinimumInformationTiers/): evidence tiers for the results of the pilots. Filter by case with the keywords (for example *case 5: metabolomics, metabolite annotations*), or by what a query uses (for example *Rhea*, *co-expression*, *gene-metabolite association*, *biosynthetic gene cluster*).

Every query of the minimum information tiers returns a **list of pathway components that reach its level of evidence**, with the putative pathway and the support (tools, features, scores, genes) as extra columns. The components are:

* **putative / supported reactions** (keyword *output: reactions*)
* **putative / supported metabolites** (keyword *output: metabolites*)
* **putative / supported genes in the same pathway** (keyword *output: genes*); the lowest tier is two genes in the same biosynthetic gene cluster

The three `ranked-pathway-*` queries (metabolites, reactions, genes) put all the evidence of a scope together as optional parts and **rank the components by a score**: the evidence is grouped into families that are not independent, and the score is the noisy-OR over the strongest tier of each family. The single-tier queries are the building blocks.

# Examples

* [SIB Swiss Institute of Bioinformatics](https://sib-swiss.github.io/sparql-examples/)
