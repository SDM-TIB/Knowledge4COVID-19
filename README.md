[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4701816.svg)](https://doi.org/10.5281/zenodo.4701816)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache2-green.svg)](LICENSE)

# Knowledge4COVID-19

## Knowledge4COVID-19 Framework
Knowledge4COVID-19 is a framework that aims to showcase the power of integrating disparate sources of knowledge to discover adverse drug effects caused by drug-drug interactions among COVID-19 treatments and pre-existing condition drugs. The Knowledge4COVID-19 framework is devised as a network of data ecosystems (DEs). It aligns [data](https://tib.eu/cloud/s/TxWtP8jpX3KRipr) and metadata to describe the network and its components. Heterogeneity issues across the different data sets are overcome by various methods of data curation and integration. Each DE comprises data sets, programs for accessing, managing, and analysing their data. Interoperability issues across a DE data sets are solved in a [unified view](https://github.com/SDM-TIB/Knowledge4COVID-19/blob/main/KGC-DIS/K4Covid-19UnifiedSchema.ttl). [Mappings](https://github.com/SDM-TIB/Knowledge4COVID-19/tree/main/KGC-DIS/CSV2RDF-RMLMappingRules) between the data sets and the unified schema describe the meaning of the data sets.

![Knowledge4COVID-19 DataEcosystem](https://github.com/SDM-TIB/Knowledge4COVID-19/blob/main/images/K4COVID-19DES.png "Knowledge4COVID-19 DE")

## Knowledge4COVID-19 DataEcosystem
Data sources from the data sources in the Knowledge4COVID-19 DE are integrated into the Knowledge4COVID-19 KG.
The following figure depicts the steps of the KG creation process.
Steps 1 and 2 are done at the level of Scientific Open Data and Publications DEs, while steps 3 and 4 are conducted at the level of Knowledge4COVID-19 DE to create the Knowledge4COVID-19 KG.
First, data is ingested and described in terms of metadata (step 1), e.g., title and abstract of the publications, and drug-drug interactions.
Knowledge extraction methods recognize biomedical entities from textual data and link them to [UMLS](https://www.nlm.nih.gov/research/umls/index.html), and to resources in [DBpedia](https://www.dbpedia.org/), [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page), [Uniprot](https://www.uniprot.org/help/uniprotkb), and [DrugBank](https://go.drugbank.com/).
A total of 12,223,409 UMLS annotations have been extracted by [FALCON](https://github.com/SDM-TIB/falcon2.0).
These annotations are used for solving entity alignment and semantic data integration of biomedical entities in the Knowledge4COVID-19 KG (e.g., drugs, phenotypes, side effects, and adverse events).
Moreover, there are 3,739,445 links to DBpedia, 3,476,435 links to Wikidata, 5,248 links to the Uniprot RDF KG, and 3,427 links to DrugBank.
The data sources shared by these DEs are mapped to the [Knowledge4COVID-19 unified schema](https://github.com/SDM-TIB/Knowledge4COVID-19/blob/main/KGC-DIS/K4Covid-19UnifiedSchema.ttl).
These definitions are declaratively specified using the RDF Mapping Language (RML).
[SDM-RDFizer](https://github.com/SDM-TIB/SDM-RDFizer) transforms these shared data into an [RDF graph](https://labs.tib.eu/sdm/covid19kg/sparql) by executing the the [RML mapping rules](https://github.com/SDM-TIB/Knowledge4COVID-19/tree/main/KGC-DIS/CSV2RDF-RMLMappingRules).
SDM-RDFizer implements optimized data structures that are exploited during the execution of RML mapping rules to speed up the KG creation process.
The Knowledge4COVID-19 KG is published following the Linked Data principles.
A [linked data interface](https://research.tib.eu/covid-19/page/entity/C0168273) using Pubby is provided; thus, all the URIs can be dereferenced.
Additionally, a [SPARQL endpoint](https://labs.tib.eu/sdm/covid19kg/sparql) allows for querying processing on top of the Knowledge4COVID-19 KG, while the federated query engine, [DeTrusty](https://github.com/SDM-TIB/DeTrusty), evaluates [SPARQL queries](https://labs.tib.eu/sdm/k4covid-query-engine/sparql) over the federation of the Knowledge4COVID-19 KG, DBpedia, Wikidata, and UniProt RDF.
Additionally, various API REST services are offered to traverse the Knowledge4COVID-19 KG, and analyze drug-drug interactions and side effects (step 4).

![Knowledge4COVID-19 KG Pipeline](https://github.com/SDM-TIB/Knowledge4COVID-19/blob/main/images/K4covidpipeline.png "Knowledge4COVID-19 Workflow")

Knowledge4COVID-19 unified schema concepts (i.e., classes and properties) are related via the [owl:equivalentClass](https://www.w3.org/TR/owl-ref/#equivalentClass-def) and [owl:equivalentProperty](https://www.w3.org/TR/owl-ref/#equivalentProperty-def) predicates to concepts in DBpedia, Wikidata, Uniprot, the Open Biological and Biomedical Ontology, the Semanticscience Integrated Ontology, and Dublin Core. In total, 17 concepts are mapped to at least one concept in these ontologies. A [VoCol instance](http://ontology.tib.eu/K4COVID-19/) is also available for Knowledge4COVID-19 unified schema. The [metadata](http://ontology.tib.eu/K4COVID-19/documentation) describing each of the depicted concepts can be accessed. 

![Knowledge4COVID-19 UnifiedSchema Classes vs Attributes](https://github.com/SDM-TIB/Knowledge4COVID-19/blob/main/images/classesVersusAttributes.png "Knowledge4COVID-19 Unified Schema Classes and Properties")
## Prediction over Knowledge4COVID-19 KG
The main goal of this work is to analyze the potential adverse effects of treatments received by COVID-19 patients in combination with other medications in the form of drug-drug interactions. In the Open Data DE, DrugBank presents an adequate source for retrieving expected interactions, explicitly providing the interactions of each drug with other drugs in a structured way. However, to enrich this initial set of drug-drug interactions, we move forward to a predictive analysis on our graph that provides an extended set of such interactions. For this purpose, we have implemented a machine learning [method](https://github.com/kbogas/DDI_BLKG) that exploits patterns unveiled from contextual information of the Scientific Publications DE to predict potential drug-drug interactions not existing in DrugBank. Our method is based on the analysis of an Open Data KG, resulting from the natural language processing and semantic indexing of biomedical publications and open resources. The Open Data KG constitutes an integral part of the Knowledge4COVID-19 KG, representing the structured information extracted from relevant publications in the form of triples. All drugs included in Drugbank are also part of this graph, relating these with specific targets, diseases, and other biomedical entities identified in literature text, through a set of semantic relations from the [UMLS Semantic Network](https://www.nlm.nih.gov/research/umls/META3_current_relations.html).

## Knowledge4COVID-19 Evaluation
<!---We illustrate the analytical support provided by Knowledge4COVID-19. We analyze relevant adverse effects that may be produced as a result of interactions among drugs to treat COVID-19 and the most common pre-existing conditions. The figure below depicts the adverse effects commonly reported during the treatments of hypertension, asthma, and diabetes: 

![AdverseEffect](https://github.com/SDM-TIB/Knowledge4COVID-19/blob/main/images/adverseEffectPerComorbidity.png "AdverseEffect")

A wide range of adverse effects may be triggered, but the top-5 most frequent affect the blood counts (e.g., Agranulocytosis, Eosinophilia, Pyuria, and Aplastic anemia), cardiovascular disorders (e.g., Thrombophlebitis and Hypotension), skim and hair problems (e.g., Alopecia, Pruritus, Exanthema), eye conditions (e.g., Glaucoma), and autoimmune disorders (e.g., Hypersensitivity). These adverse effects may be worsened during a SARS-CoV-2 infection, thus, patients with suffering from these pre-existing conditions should be carefully treated. 
Additionally, we evaluate the effects of the interactions (DDIs) between the drugs used to treat hypertension and COVID-19:
![Hypertensive](https://github.com/SDM-TIB/Knowledge4COVID-19/blob/main/images/Hypertensive.png "Hypertensive")

As observed, a large number of DDIs may exist and generate serious conditions like QT prolongation. They results suggest that COVID-19 patients receiving treatments for pre-existing conditions need to be carefully treated.--->

The Knowledge4COVID-19 KG is a unique source of knowledge to identify patterns in the integrated networks of interactions, biomedical entities, and publications, e.g. adverse events generated by combining COVID-19 drugs and drugs prescribed for pre-existing conditions. We analyse and evaluate the drug-drug interactions that can be deduced over the Knowledge4COVID-19 KG and the effects of these interactions. A more detailed analysis of the impact of the combination of drugs can be executed on the public [available Jupyter Notebook](https://colab.research.google.com/drive/146-oQTxDpZQoOifKY6iafaEwuupH7q3t#scrollTo=ZMmLkkoE9XO0). Also, exemplar DDIs represented in the Knowledge4COVID-19 KG can also be [visualized](https://youtu.be/7YsTYJzRfR0). 
