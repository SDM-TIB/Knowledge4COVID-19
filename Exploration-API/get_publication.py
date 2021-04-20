#!/usr/bin/env python
# coding: utf-8


from SPARQLWrapper import SPARQLWrapper, JSON

def load_drug_cui(data):
    input_cui = data['Drugs']
    input_cui_uri = ','.join(['<http://covid-19.tib.eu/Annotation/'+cui+'>' for cui in input_cui])
    return input_cui_uri


def get_publication(input_cui_uri, sparql):
    query = """
    select distinct ?pub ?year ?journal ?title ?doi ?cui_annotation ?cui_label
            where {

                ?ConceptAnnotation a <http://covid-19.tib.eu/vocab/ConceptAnnotation>.
                ?ConceptAnnotation <http://covid-19.tib.eu/vocab/annotates> ?pub .
                ?ConceptAnnotation <http://covid-19.tib.eu/vocab/hasSemanticAnnotation> ?SemanticAnnotation.
                ?SemanticAnnotation <http://covid-19.tib.eu/vocab/hasCUIAnnotation> ?cui_annotation .
                ?cui_annotation <http://covid-19.tib.eu/vocab/annLabel> ?cui_label .

                ?pub <http://covid-19.tib.eu/vocab/title> ?title .
                ?pub <http://covid-19.tib.eu/vocab/year> ?year .
                ?pub <http://covid-19.tib.eu/vocab/journal> ?journal .
                ?pub <http://covid-19.tib.eu/vocab/doi> ?doi .

                Filter(?cui_annotation in (""" + input_cui_uri + """))
    }
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    dictionary = {}
    dictionary['Publication:'] = {}
    for r in results['results']['bindings']:
        pub = (r['pub']['value']).replace('http://covid-19.tib.eu/Publication/', '')
        year = r['year']['value']
        journal = r['journal']['value']
        title = r['title']['value']
        url = r['doi']['value']
        drug = (r['cui_annotation']['value']).replace('http://covid-19.tib.eu/Annotation/', '')
        drugLabel = r['cui_label']['value']

        if pub not in dictionary['Publication:']:
            dictionary['Publication:'][pub] = {}
            dictionary['Publication:'][pub]['year:'] = year
            dictionary['Publication:'][pub]['journal:'] = journal
            dictionary['Publication:'][pub]['title:'] = title
            dictionary['Publication:'][pub]['doi:'] = url
            dictionary['Publication:'][pub]['cui_annotation:'] = []
            dictionary['Publication:'][pub]['cui_label:'] = []
            dictionary['Publication:'][pub]['cui_annotation:'].append(drug)
            dictionary['Publication:'][pub]['cui_label:'].append(drugLabel)
        else:
            dictionary['Publication:'][pub]['cui_annotation:'].append(drug)
            dictionary['Publication:'][pub]['cui_label:'].append(drugLabel)

    return dictionary

def process(input_dicc,endpoint):
    sparql = SPARQLWrapper(endpoint)
    input_cui_uri = load_drug_cui(input_dicc)
    return get_publication(input_cui_uri, sparql)
