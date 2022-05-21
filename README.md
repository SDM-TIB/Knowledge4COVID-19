# Knowledge4COVID-19

## Knowledge4COVID-19 Framework
Knowledge4COVID-19 is a framework that aims to showcase the power of integrating disparate sources of knowledge to discover adverse drug effects caused by drug-drug interactions among COVID-19 treatments and pre-existing condition drugs. The Knowledge4COVID-19 framework is devised as a network of data ecosystems (DEs). It aligns [data](https://tib.eu/cloud/s/dfzsdM8eEXxwf5m) and metadata to describe the network and its components. Heterogeneity issues across the different data sets are overcome by various methods of data curation and integration. Each DE comprises data sets, programs for accessing, managing, and analysing their data. Interoperability issues across a DE data sets are solved in a [unified view](https://github.com/SDM-TIB/Knowledge4COVID-19/blob/main/KGC-DIS/K4Covid-19UnifiedSchema.ttl). [Mappings](https://github.com/SDM-TIB/Knowledge4COVID-19/tree/main/KGC-DIS/CSV2RDF-RMLMappingRules) between the data sets and the unified schema describe the meaning of the data sets.

![Knowledge4COVID-19 DataEcosystem](https://github.com/SDM-TIB/Knowledge4COVID-19/blob/main/images/K4COVID-19DES.png "Knowledge4COVID-19 DE")

## Knowledge4COVID-19 DataEcosystem
Data sources from the data sources in the Knowledg4COVID-19 DE are integrated into the Knowledg4COVID-19 KG. The following figure depicts the steps of the KG creation process. Steps 1 and 2 are done at the level of Scientific Open Data and Publications DEs, while steps 3 and 4 are conducted Knowledg4COVID-19 DE. First, data is ingested and described in terms of metadata, e.g., title and abstract of the publications. Knowledge extraction methods (e.g., entity recognition and linking) extract biomedical entities from textual data and link the recognized entities to terms in biomedical vocabularies (e.g., [UMLS](https://www.nlm.nih.gov/research/umls/index.html)) and resources in [DBpedia](https://www.dbpedia.org/), [Bio2RDF](https://bio2rdf.org/), and [DrugBank](https://go.drugbank.com/). A total of 3,822,265 annotations have been extracted. There are 7,344 and 11,292 links to DBpedia and Bio2RDF. Also, there are 11,292 external links to DrugBank. The data sources shared by these DEs are mapped to the [Knowledge4COVID-19 unified schema](http://ontology.tib.eu/K4COVID-19/). These definitions are declaratively specified using the RDF Mapping Language (RML). [SDM-RDFizer](https://github.com/SDM-TIB/SDM-RDFizer) transforms these shared data into an [RDF graph](https://labs.tib.eu/sdm/covid19kg/sparql) by executing the the [RML mapping rules](https://github.com/SDM-TIB/Knowledge4COVID-19/tree/main/KGC-DIS/CSV2RDF-RMLMappingRules). SDM-RDFizer implements optimized data structures that are exploited during the execution of RML mapping rules to speed up the KG creation process. The Knowledge4COVID-19 KG is published following the Linked Data principles. A [linked data interface](https://research.tib.eu/covid-19/page/entity/C0168273) using Pubby is provided; thus, all the URIs can be dereferenced. Additionally, a SPARQL endpoint allows for querying processing on top of the Knowledge4COVID-19 KG, while the [federated query engine](https://labs.tib.eu/sdm/k4covid-query-engine/sparql), DeTrusty, evaluates SPARQL queries over the federation of the Knowledge4COVID-19 KG, DBpedia, Wikidata, and UniProt RDF. Additionally, various API REST services are offered to traverse the Knowledge4COVID-19 KG, and analyze drug-drug interactions and side effects (step 4).

![Knowledge4COVID-19 KG Pipeline](https://github.com/SDM-TIB/Knowledge4COVID-19/blob/main/images/K4covidpipeline.png "Knowledge4COVID-19 Workflow")

## Prediction over Knowledge4COVID-19 KG
The main goal of this work is to analyze the potential adverse effects of treatments received by COVID-19 patients in combination with other medications in the form of drug-drug interactions. In the Open Data DE, DrugBank presents an adequate source for retrieving expected interactions, explicitly providing the interactions of each drug with other drugs in a structured way. However, to enrich this initial set of drug-drug interactions, we move forward to a predictive analysis on our graph that provides an extended set of such interactions. For this purpose, we have implemented a machine learning [method](https://github.com/kbogas/DDI_BLKG) that exploits patterns unveiled from contextual information of the Scientific Publications DE to predict potential drug-drug interactions not existing in DrugBank. Our method is based on the analysis of an Open Data KG, resulting from the natural language processing and semantic indexing of biomedical publications and open resources. The Open Data KG constitutes an integral part of the Knowledge4COVID-19 KG, representing the structured information extracted from relevant publications in the form of triples. All drugs included in Drugbank are also part of this graph, relating these with specific targets, diseases, and other biomedical entities identified in literature text, through a set of semantic relations from the [UMLS Semantic Network](https://www.nlm.nih.gov/research/umls/META3_current_relations.html).

## Knowledge4COVID-19 Evaluation
We illustrate the analytical support provided by Knowledge4COVID-19. We analyze relevant adverse effects that may be produced as a result of interactions among drugs to treat COVID-19 and the most common pre-existing conditions. The figure below depicts the adverse effects commonly reported during the treatments of hypertension, asthma, and diabetes: 

![AdverseEffect](https://github.com/SDM-TIB/Knowledge4COVID-19/blob/main/images/adverseEffectPerComorbidity.png "AdverseEffect")

A wide range of adverse effects may be triggered, but the top-5 most frequent affect the blood counts (e.g., Agranulocytosis, Eosinophilia, Pyuria, and Aplastic anemia), cardiovascular disorders (e.g., Thrombophlebitis and Hypotension), skim and hair problems (e.g., Alopecia, Pruritus, Exanthema), eye conditions (e.g., Glaucoma), and autoimmune disorders (e.g., Hypersensitivity). These adverse effects may be worsened during a SARS-CoV-2 infection, thus, patients with suffering from these pre-existing conditions should be carefully treated. 
Additionally, we evaluate the effects of the interactions (DDIs) between the drugs used to treat hypertension and COVID-19:
![Hypertensive](https://github.com/SDM-TIB/Knowledge4COVID-19/blob/main/images/Hypertensive.png "Hypertensive")

As observed, a large number of DDIs may exist and generate serious conditions like QT prolongation. They results suggest that COVID-19 patients receiving treatments for pre-existing conditions need to be carefully treated. 
A more detailed analysis of the impact of the combination of drugs can be executed on the public [available Jupyter Notebook](https://colab.research.google.com/drive/146-oQTxDpZQoOifKY6iafaEwuupH7q3t#scrollTo=ZMmLkkoE9XO0). Also, exemplar DDIs represented in the Knowledge4COVID-19 KG can also be [visualized](https://youtu.be/7YsTYJzRfR0). 
