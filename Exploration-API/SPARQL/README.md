# Knowledge4COVID-19 KG-Exploration API SPARQL Queries:

# Publications related to drugs

```
PREFIX k4covid: <http://research.tib.eu/covid-19/vocab/>
PREFIX k4covide: <http://research.tib.eu/covid-19/entity/>
SELECT DISTINCT ?pub ?year ?journal ?title ?url ?drug ?drugLabel where {
        ?drug a k4covid:Drug.
        ?drug k4covid:hasCUIAnnotation ?drugCUI.
        Filter(?drugCUI in (k4covide:C0031623,
        k4covide:C0751995,
        k4covide:C0030106))
        ?drugCUI k4covid:annLabel ?drugLabel.
        ?ann a k4covid:ConceptAnnotation.
        ?ann k4covid:hasSemanticAnnotation ?semAnn.
        ?semAnn k4covid:hasCUIAnnotation ?drugCUI.
        ?ann k4covid:annotates ?pub.
        ?pub <http://purl.org/dc/terms/title> ?title.
        ?pub k4covid:year ?year.
        ?pub k4covid:journal ?journal.
        ?pub k4covid:externalLink ?url.
```

# Drug-Drug Interactions (DDI)
## Get Interactions of a Drug

```
PREFIX k4covid: <http://research.tib.eu/covid-19/vocab/>
PREFIX k4covide: <http://research.tib.eu/covid-19/entity/>
SELECT DISTINCT ?effectorDrugLabel ?affectdDrugLabel ?effect AS ?effectLabel  ?impactLabel   WHERE {  
    ?interaction k4covid:precipitantDrug ?effectorDrugCUI.
    ?interaction k4covid:objectDrug ?affectdDrugCUI.
    ?effectorDrugCUI k4covid:annLabel ?effectorDrugLabel.
    ?affectdDrugCUI k4covid:annLabel ?affectdDrugLabel.
    ?interaction k4covid:effect ?effectCUI.
    ?effectCUI k4covid:annLabel  ?effect.
    ?interaction k4covid:impact ?impactLabel.                                   
FILTER(?affectdDrugCUI in (k4covide:C0000970))}
```

## Get all the interaction among the provided Drugs

```
PREFIX k4covid: <http://research.tib.eu/covid-19/vocab/>
PREFIX k4covide: <http://research.tib.eu/covid-19/entity/>
SELECT * {
{SELECT DISTINCT ?effectorDrugLabel ?affectdDrugLabel ?effect AS ?effectLabel ?impactLabel  WHERE {
    ?interaction k4covid:precipitantDrug k4covide:C0000970.
    ?interaction k4covid:objectDrug k4covide:C0028978.
    k4covide:C0000970 k4covid:annLabel ?effectorDrugLabel.
    k4covide:C0028978 k4covid:annLabel ?affectdDrugLabel.                 
    ?interaction k4covid:effect ?effectCUI.
    ?effectCUI k4covid:annLabel ?effect.
    ?interaction k4covid:impact ?impactLabel.     
}} UNION 
{SELECT DISTINCT ?effectorDrugLabel ?affectdDrugLabel ?effect AS ?effectLabel ?impactLabel  WHERE {  
    ?interaction k4covid:precipitantDrug k4covide:C0028978.
    ?interaction k4covid:objectDrug k4covide:C0000970.
    k4covide:C0028978 k4covid:annLabel ?effectorDrugLabel.
    k4covide:C0000970 k4covid:annLabel ?affectdDrugLabel.                                        
    ?interaction k4covid:effect ?effectCUI.
    ?effectCUI k4covid:annLabel ?effect.
    ?interaction k4covid:impact ?impactLabel.
}}}                                     

```

# Predicted Drug-Drug Interactions

## Get the predicted interactions of a Drug

```
PREFIX k4covid: <http://research.tib.eu/covid-19/vocab/>
PREFIX k4covide: <http://research.tib.eu/covid-19/entity/>
SELECT DISTINCT ?effectorDrugLabel ?affectdDrugLabel ?confidence ?provenance WHERE {  
    ?interaction a k4covid:DrugDrugPrediction.
    ?interaction k4covid:hasInteractingDrug ?effectorDrug.
    ?interaction k4covid:hasInteractingDrug ?affectedDrug.
    FILTER (?effectorDrug != ?affectedDrug)
    ?affectedDrug k4covid:hasCUIAnnotation ?affectdDrugCUI.
    ?effectorDrug k4covid:hasCUIAnnotation ?effectorDrugCUI.
    ?effectorDrugCUI k4covid:annLabel ?effectorDrugLabel.
    ?affectdDrugCUI k4covid:annLabel ?affectdDrugLabel.
    ?interaction k4covid:confidence ?confidence.
    ?interaction k4covid:predictionMethod ?provenance.                                
FILTER(?affectdDrugCUI in (k4covide:C0000970))}
```

# Get all the interaction among the provided Drugs
```
PREFIX k4covid: <http://research.tib.eu/covid-19/vocab/>
PREFIX k4covide: <http://research.tib.eu/covid-19/entity/>
SELECT * {
{SELECT DISTINCT ?effectorDrugLabel ?affectdDrugLabel ?confidence ?provenance  WHERE {
    ?interaction k4covid:hasInteractingDrug ?effectorDrug.
    ?interaction k4covid:hasInteractingDrug ?affectedDrug.
    FILTER (?effectorDrug != ?affectedDrug)
    ?effectorDrug k4covid:hasCUIAnnotation k4covide:C0995188.
    ?affectedDrug k4covid:hasCUIAnnotation k4covide:C0765273.
    k4covide:C0000970 k4covid:annlabel ?effectorDrugLabel.
    k4covide:C0009214 k4covid:annlabel ?affectdDrugLabel.
    ?interaction k4covid:confidence ?confidence.
    ?interaction k4covid:predictionMethod ?provenance.       
}} UNION 
{SELECT DISTINCT ?effectorDrugLabel ?affectdDrugLabel ?confidence ?provenance  WHERE {  
    ?interaction k4covid:hasInteractingDrug ?effectorDrug.
    ?interaction k4covid:hasInteractingDrug ?affectedDrug.
    FILTER (?effectorDrug != ?affectedDrug)
    ?effectorDrug k4covid:hasCUIAnnotation k4covide:C0765273.
    ?affectedDrug k4covid:hasCUIAnnotation k4covide:C0995188.
    k4covide:C0009214 k4covid:annLabel ?effectorDrugLabel.
    k4covide:C0000970 k4covid:annLabel ?affectdDrugLabel.
    ?interaction k4covid:confidence ?confidence.
    ?interaction k4covid:predictionMethod ?provenance.    
}}}               
```
