#!/usr/bin/env python
# coding: utf-8


from SPARQLWrapper import SPARQLWrapper, JSON

def load_drug_cui(data):
    input_cui = data['Drugs']
    input_cui_uri = ','.join(['<http://covid-19.tib.eu/Annotation/'+cui+'>' for cui in input_cui])
    return input_cui_uri


def get_publication(input_cui_uri, sparql):
    query = """
    select distinct ?pub ?year ?journal ?title ?url ?drug ?drugLabel where {
        ?drug a <http://covid-19.tib.eu/vocab/Drug>.
        ?drug <http://covid-19.tib.eu/vocab/hasCUIAnnotation> ?drugCUI.
        Filter(?drugCUI in (""" + input_cui_uri + """))
        ?drug <http://covid-19.tib.eu/vocab/drugLabel> ?drugLabel.
        ?ann a <http://covid-19.tib.eu/vocab/ConceptAnnotation>.
        ?ann <http://covid-19.tib.eu/vocab/hasSemanticAnnotation> ?semAnn.
        ?semAnn <http://covid-19.tib.eu/vocab/hasCUIAnnotation> ?drugCUI.
        ?ann <http://covid-19.tib.eu/vocab/annotates> ?pub.
        ?pub <http://covid-19.tib.eu/vocab/title> ?title.
        ?pub <http://covid-19.tib.eu/vocab/year> ?year.
        ?pub <http://covid-19.tib.eu/vocab/journal> ?journal.
        ?pub <http://covid-19.tib.eu/vocab/externalLink> ?url.

       
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
        url = r['url']['value']
        drug = (r['drug']['value']).replace('http://covid-19.tib.eu/vocab/', '')
        drugLabel = r['drugLabel']['value']

        if pub not in dictionary['Publication:']:
            dictionary['Publication:'][pub] = {}
            dictionary['Publication:'][pub]['year:'] = year
            dictionary['Publication:'][pub]['journal:'] = journal
            dictionary['Publication:'][pub]['title:'] = title
            dictionary['Publication:'][pub]['url:'] = url
            dictionary['Publication:'][pub]['Drug:'] = []
            dictionary['Publication:'][pub]['DrugLabel:'] = []
            dictionary['Publication:'][pub]['Drug:'].append(drug)
            dictionary['Publication:'][pub]['DrugLabel:'].append(drugLabel)
        else:
            dictionary['Publication:'][pub]['Drug:'].append(drug)
            dictionary['Publication:'][pub]['DrugLabel:'].append(drugLabel)

    '''with open('publication.json', 'w') as fp:
        json.dump(dictionary, fp)'''
    return dictionary

def process(input_dicc,endpoint):
    sparql = SPARQLWrapper(endpoint)
    input_cui_uri = load_drug_cui(input_dicc)
    return get_publication(input_cui_uri, sparql)
