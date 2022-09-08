# Knowledge4COVID-19 Federated Query Engine

We resort to the federated query engine [DeTrusty](https://github.com/SDM-TIB/DeTrusty) to execute federated queries over the [Knowledge4COVID-19 KG](https://labs.tib.eu/sdm/covid19kg/sparql), DBpedia, Wikidata, and UniProt RDF.


| Reference             | Link                                                                                                       |
|-----------------------|------------------------------------------------------------------------------------------------------------|
| DeTrusty GitHub       | [https://github.com/SDM-TIB/DeTrusty](https://github.com/SDM-TIB/DeTrusty)                                 |
| DeTrusty Instance     | [https://labs.tib.eu/sdm/k4covid-query-engine/sparql](https://labs.tib.eu/sdm/k4covid-query-engine/sparql) |
| Knowledge4COVID-19 KG | [https://labs.tib.eu/sdm/covid19kg/sparql](https://labs.tib.eu/sdm/covid19kg/sparql)                       |

## Examples for Federated Queries

### Example Query Q1
Q1: "_Retrieve from DBpedia the excretion rate, the metabolism, and the routes of administration of the COVID-19 drugs in the treatments to treat COVID-19 in patients with Asthma._"

```
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX k4covid: <http://research.tib.eu/covid-19/vocab/>
PREFIX k4covide: <http://research.tib.eu/covid-19/entity/>

SELECT DISTINCT ?treatment ?sameAsCovidDrug ?excretation ?metabolism ?routes WHERE {
  SERVICE <https://labs.tib.eu/sdm/covid19kg/sparql> {
    ?treatment k4covid:hasCovidDrug ?covidDrug.
    FILTER( ?comorbidity=k4covide:Asthma )
    ?treatment k4covid:hasComorbidity ?comorbidity.
    ?treatment k4covid:hasComorbidityDrug ?comorbidityDrug.
    ?comorbidityDrug k4covid:hasCUIAnnotation ?CUIComorbidityDrug.
    ?CUIComorbidityDrug owl:sameAs ?sameAsComorbidityDrug .
    ?covidDrug k4covid:hasCUIAnnotation ?CUICovidDrug.
    ?CUICovidDrug owl:sameAs ?sameAsCovidDrug .
  }
  SERVICE <https://dbpedia.org/sparql> {
    ?sameAsCovidDrug dbp:excretion ?excretation.
    ?sameAsCovidDrug dbp:metabolism ?metabolism.
    ?sameAsCovidDrug dbp:routesOfAdministration ?routes.
  }  
} ORDER BY ?treatment
```

### Example Query Q2
Q2: "_Retrieve from Wikidata the CheMBL code, the metabolism, and the routes of administration of the COVID-19 drugs in the treatments to treat COVID-19 in patients with Cardiopathy._"

```
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX k4covid: <http://research.tib.eu/covid-19/vocab/>
PREFIX k4covide: <http://research.tib.eu/covid-19/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

SELECT DISTINCT ?treatment ?sameAsComorbidityDrug ?idDrug ?activeIngredient ?mass
WHERE {
  SERVICE <https://labs.tib.eu/sdm/covid19kg/sparql> {
    ?treatment k4covid:hasCovidDrug ?covidDrug.
    ?treatment k4covid:hasComorbidity k4covide:Cardiopathy .
    ?treatment k4covid:hasComorbidityDrug ?comorbidityDrug.
    ?comorbidityDrug k4covid:hasCUIAnnotation ?CUIComorbidityDrug.
    ?CUIComorbidityDrug owl:sameAs ?sameAsComorbidityDrug .
    ?covidDrug k4covid:hasCUIAnnotation ?CUICovidDrug.
    ?CUICovidDrug owl:sameAs ?sameAsCovidDrug .
  }
  SERVICE <https://query.wikidata.org/sparql> {
    ?sameAsComorbidityDrug wdt:P592 ?idDrug .
    ?sameAsComorbidityDrug wdt:P3780 ?activeIngredient . 
    ?sameAsComorbidityDrug  wdt:P2067 ?mass .
  }
}
```

### Example Query Q3
Q3: "_Retrieve from DBpedia the excretion rate, the metabolism, and the routes of administration, CheMBL and Kegg codes, the smile notation, and trade name of the COVID-19 drugs in the treatments to treat COVID-19 in patients with Asthma._"

```
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX k4covid: <http://research.tib.eu/covid-19/vocab/>
PREFIX k4covide: <http://research.tib.eu/covid-19/entity/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>

SELECT DISTINCT ?treatment ?sameAsCovidDrug ?excretation ?metabolism ?routes ?dbCheml ?dbKegg ?dbDrugBank ?dbSmiles ?tradeName
WHERE {
  SERVICE <https://labs.tib.eu/sdm/covid19kg/sparql> {
    ?treatment k4covid:hasCovidDrug ?covidDrug.
    ?treatment k4covid:hasComorbidity k4covide:Asthma.
    ?treatment k4covid:hasComorbidityDrug ?comorbidityDrug.
    ?comorbidityDrug k4covid:hasCUIAnnotation ?CUIComorbidityDrug.
    ?CUIComorbidityDrug owl:sameAs ?sameAsComorbidityDrug .
    ?covidDrug k4covid:hasCUIAnnotation ?CUICovidDrug.
    ?CUICovidDrug owl:sameAs ?sameAsCovidDrug .
  }
 SERVICE <https://dbpedia.org/sparql> {
    ?sameAsCovidDrug dbp:excretion ?excretation.
    ?sameAsCovidDrug dbp:metabolism ?metabolism.
    ?sameAsCovidDrug dbp:routesOfAdministration ?routes.
    ?sameAsCovidDrug dbo:chEMBL ?dbCheml.
    ?sameAsCovidDrug dbo:kegg ?dbKegg.
    ?sameAsCovidDrug dbo:drugbank ?dbDrugBank .
    ?sameAsCovidDrug dbp:smiles ?dbSmiles .
    ?sameAsCovidDrug dbp:tradename ?tradeName.
  } 
} ORDER BY ?treatment
```

### Example Query Q4
Q4: "_Retrieve from DBpedia the disease label, ICD-10 and mesh codes, and risks of the comorbidities of the COVID-19 treatments._"

```
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX k4covid: <http://research.tib.eu/covid-19/vocab/>
PREFIX k4covide: <http://research.tib.eu/covid-19/entity/>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>

SELECT DISTINCT ?sameAsComorbidity ?disease ?icd10 ?risk WHERE {
  SERVICE <https://labs.tib.eu/sdm/covid19kg/sparql> {
    ?treatment k4covid:hasCovidDrug ?covidDrug.
    ?treatment k4covid:hasComorbidity ?comorbidity.
    ?comorbidity k4covid:hasCUIAnnotation ?annotationComorbidity .
    ?annotationComorbidity owl:sameAs ?sameAsComorbidity
  }
  SERVICE <https://dbpedia.org/sparql> {
    ?sameAsComorbidity dbo:diseasesDB ?disease.
    ?sameAsComorbidity dbo:icd10 ?icd10. 
    ?sameAsComorbidity dbo:meshId ?meshID .
    ?sameAsComorbidity dbp:risks ?risk 
  }
}
```

### Example Query Q5
Q5: "_Retrieve the COVID-19 and comorbidity drugs on a treatment and the CheMBL, mass, and excretion route for the comorbidity drugs._"

```
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX k4covid: <http://research.tib.eu/covid-19/vocab/>
PREFIX k4covide: <http://research.tib.eu/covid-19/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

SELECT DISTINCT ?treatment ?sameAsComorbidityDrug ?sameAsCovidDrug ?idDrug ?mass ?excretation
WHERE {
  SERVICE <https://labs.tib.eu/sdm/covid19kg/sparql> {
    ?treatment k4covid:hasCovidDrug ?covidDrug.
    ?treatment k4covid:hasComorbidity k4covide:Cardiopathy .
    ?treatment k4covid:hasComorbidityDrug ?comorbidityDrug.
    ?comorbidityDrug k4covid:hasCUIAnnotation ?CUIComorbidityDrug.
    ?CUIComorbidityDrug owl:sameAs ?sameAsComorbidityDrug .
    ?covidDrug k4covid:hasCUIAnnotation ?CUICovidDrug.
    ?CUICovidDrug owl:sameAs ?sameAsCovidDrug .
  }
  {
    SERVICE <https://query.wikidata.org/sparql> {
      ?sameAsComorbidityDrug wdt:P592 ?idDrug .
      ?sameAsComorbidityDrug wdt:P2067 ?mass .
    }
  }
  UNION
  {
    SERVICE <https://dbpedia.org/sparql> {
      ?sameAsComorbidityDrug dbp:excretion ?excretation . 
    }
  }
}
```
