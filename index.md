# SPARQL examples

Queries for the PlantMetWiki knowledge graph that define evidence tiers. A query that uses data of several cases is listed under each of them. Use the keywords in the tables of the folders to filter by what a query uses (for example Rhea, co-expression, gene-metabolite association, biosynthetic gene cluster).

* [PlantMetWiki](./examples/PlantMetWiki/): evidence tiers of pathway components (EC number, Rhea, UniProt, enzyme nodes, orthologs)
* [Minimum information tiers](./examples/MinimumInformationTiers/): evidence tiers for the results of the pilots, by case

1. New pathway from the literature
   * no queries yet
2. Inferred enzyme function from PMN/PlantCyc+ db
   * [the difference between two metabolites is a Rhea reaction with a PlantMetWiki enzyme](./examples/MinimumInformationTiers/rhea-step-between-metabolites.md)
   * [gene is predicted to catalyse the transformation between the two metabolites](./examples/MinimumInformationTiers/gene-catalyses-the-transformation.md)
   * see also the [PlantMetWiki](./examples/PlantMetWiki/) tiers of pathway components
3. plantiSMASH-predicted BGCs: predicted gene clusters
   * [co-expressed genes are in the same biosynthetic gene cluster](./examples/MinimumInformationTiers/coexpressed-in-same-cluster.md)
   * [co-expressed genes in the same cluster, one matches a pathway](./examples/MinimumInformationTiers/coexpressed-in-cluster-one-in-pathway.md)
   * [co-expressed genes in the same cluster, both match a pathway](./examples/MinimumInformationTiers/coexpressed-in-cluster-both-in-pathway.md)
4. Transcriptomics: gene coexpression values
   * [co-expressed genes are in the same biosynthetic gene cluster](./examples/MinimumInformationTiers/coexpressed-in-same-cluster.md)
   * [co-expressed genes in the same cluster, one matches a pathway](./examples/MinimumInformationTiers/coexpressed-in-cluster-one-in-pathway.md)
   * [co-expressed genes in the same cluster, both match a pathway](./examples/MinimumInformationTiers/coexpressed-in-cluster-both-in-pathway.md)
5. Metabolomics: metabolite annotations
   * [annotation matches PlantMetWiki (first InChIKey block)](./examples/MinimumInformationTiers/annotation-matches-plantmetwiki.md)
   * [two metabolites share a chemical class](./examples/MinimumInformationTiers/shared-chemical-class.md)
   * [two metabolites linked by a similarity metric](./examples/MinimumInformationTiers/similarity-link.md)
   * [two metabolites linked by structure similarity (InChI)](./examples/MinimumInformationTiers/structure-similarity.md)
   * [the difference between two metabolites is a Rhea reaction with a PlantMetWiki enzyme](./examples/MinimumInformationTiers/rhea-step-between-metabolites.md)
   * [gene and metabolite match the same pathway](./examples/MinimumInformationTiers/gene-and-metabolite-in-same-pathway.md)
   * [gene is predicted to catalyse the transformation between the two metabolites](./examples/MinimumInformationTiers/gene-catalyses-the-transformation.md)
6. Paired omics: transcript-metabolite associations
   * [gene and metabolite match the same pathway](./examples/MinimumInformationTiers/gene-and-metabolite-in-same-pathway.md)
   * [gene of an association is in a PlantMetWiki pathway](./examples/MinimumInformationTiers/gene-in-plantmetwiki-pathway.md)
   * [gene is an ortholog of a gene of a species that has the pathway](./examples/MinimumInformationTiers/ortholog-in-pathway-species.md)
   * [gene is predicted to catalyse the transformation between the two metabolites](./examples/MinimumInformationTiers/gene-catalyses-the-transformation.md)
   * [ortholog in a pathway species and a machine-learning predicted transformation](./examples/MinimumInformationTiers/ortholog-plus-ml-prediction.md)
   * [co-expressed genes are in the same biosynthetic gene cluster](./examples/MinimumInformationTiers/coexpressed-in-same-cluster.md)
   * [co-expressed genes in the same cluster, one matches a pathway](./examples/MinimumInformationTiers/coexpressed-in-cluster-one-in-pathway.md)
   * [co-expressed genes in the same cluster, both match a pathway](./examples/MinimumInformationTiers/coexpressed-in-cluster-both-in-pathway.md)
7. "Unsupervised" GNN predictions of reactions (conversion steps)
   * [ortholog in a pathway species and a machine-learning predicted transformation](./examples/MinimumInformationTiers/ortholog-plus-ml-prediction.md)
