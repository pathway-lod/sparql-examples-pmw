# SPARQL examples

SPARQL queries for the PlantMetWiki knowledge graph that define **evidence tiers**: for the components of PlantMetWiki pathways, and as a **Minimum Information** standard for the results of the pilot data sets. Each query is one Turtle file in the SIB SPARQL-examples format; many are federated with Rhea, UniProt and OrthoDB. Use the keywords of the tables (for example *Rhea*, *co-expression*, *gene-metabolite association*, *biosynthetic gene cluster*) to filter.

# Minimum Information: evidence tiers

Grouped by the seven cases of the project. The tiers are drafts for discussion ([minimum_information](https://github.com/pathway-lod/lod-pathways-community/tree/main/minimum_information) and [prioritization](https://github.com/pathway-lod/lod-pathways-community/tree/main/prioritization) in lod-pathways-community). The connectivity to PlantMetWiki (which metabolite, gene or pathway a result matches) is **computed in the queries**, not stored as terms in the data.

| Case | Queries |
|---|---|
| 1. New pathway from the literature | no tiers yet |
| 2. Inferred enzyme function from PMN/PlantCyc+ | [Evidence tiers of pathway components](./examples/PlantMetWiki/): EC number, Rhea, UniProt, enzyme nodes, OrthoDB orthologs |
| 3. plantiSMASH-predicted BGCs: predicted gene clusters | [Minimum Information, case 3 (BGC-1 to BGC-3)](./examples/MinimumInformation_Case3_BGC/) |
| 4. Transcriptomics: gene co-expression values | used inside the BGC and paired-omics tiers (no separate tier yet) |
| 5. Metabolomics: metabolite annotations | [Minimum Information, case 5 (MET-1 to MET-5)](./examples/MinimumInformation_Case5_Metabolomics/) |
| 6. Paired omics: transcript-metabolite associations | [Minimum Information, case 6 (PO-1 to PO-4)](./examples/MinimumInformation_Case6_PairedOmics/) |
| 7. "Unsupervised" GNN predictions of reactions (conversion steps) | used in PO-4; no separate tier yet |

Queries marked *no data yet* in their keywords are written against the proposed data model and return no rows on the current evidence graphs. The others run on the evidence graphs of the pilots loaded into a local store (target `https://pathway-lod.github.io/sparql-examples-pmw/evidence-graph`), with PlantMetWiki, Rhea and UniProt called by `SERVICE`; see the README of the repository.

# Examples

* [SIB Swiss Institute of Bioinformatics](https://sib-swiss.github.io/sparql-examples/)
