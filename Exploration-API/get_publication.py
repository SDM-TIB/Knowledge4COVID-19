#!/usr/bin/env python
# coding: utf-8


from SPARQLWrapper import SPARQLWrapper, JSON

def load_drug_cui(data):
    input_cui = data['Drugs']
    input_cui_uri = ','.join(['<http://research.tib.eu/covid-19/entity/'+cui+'>' for cui in input_cui])
    return input_cui_uri


def get_publication(input_cui_uri, sparql):
    query = """
    select distinct ?pub ?year ?journal ?title ?url ?drug ?drugLabel where {
        ?drug a <http://research.tib.eu/covid-19/vocab/Drug>.
        ?drug <http://research.tib.eu/covid-19/vocab/hasCUIAnnotation> ?drugCUI.
        Filter(?drugCUI in (""" + input_cui_uri + """))
        ?drugCUI <http://research.tib.eu/covid-19/vocab/annLabel> ?drugLabel.
        ?ann a <http://research.tib.eu/covid-19/vocab/ConceptAnnotation>.
        ?ann <http://research.tib.eu/covid-19/vocab/hasSemanticAnnotation> ?semAnn.
        ?semAnn <http://research.tib.eu/covid-19/vocab/hasCUIAnnotation> ?drugCUI.
        ?ann <http://research.tib.eu/covid-19/vocab/annotates> ?pub.
        ?pub <http://purl.org/dc/terms/title> ?title.
        ?pub <http://research.tib.eu/covid-19/vocab/year> ?year.
        ?pub <http://research.tib.eu/covid-19/vocab/journal> ?journal.
        ?pub <http://research.tib.eu/covid-19/vocab/externalLink> ?url.

       
    }
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    dictionary = {}
    dictionary['Publication:'] = {}
    for r in results['results']['bindings']:
        pub = (r['pub']['value']).replace('http://research.tib.eu/covid-19/Publication/', '')
        year = r['year']['value']
        journal = r['journal']['value']
        title = r['title']['value']
        url = r['url']['value']
        drug = (r['drug']['value']).replace('http://research.tib.eu/covid-19/vocab/', '')
        drugLabel = r['drugLabel']['value']
        #drugLabel=[x.upper() for x in drugLabel]
        #drugLabel=list(set(drugLabel))
        #drugLabel=drugLabel[0]

        #if pub not in dictionary['Publication:']:
        dictionary['Publication:'][pub] = {}
        dictionary['Publication:'][pub]['year:'] = year
        dictionary['Publication:'][pub]['journal:'] = journal
        dictionary['Publication:'][pub]['title:'] = title
        dictionary['Publication:'][pub]['url:'] = url
        dictionary['Publication:'][pub]['Drug:'] = []
        dictionary['Publication:'][pub]['DrugLabel:'] = []
        dictionary['Publication:'][pub]['Drug:'].append(drug)
        dictionary['Publication:'][pub]['DrugLabel:'].append(drugLabel)
        #else:
            #dictionary['Publication:'][pub]['Drug:'].append(drug)
            #dictionary['Publication:'][pub]['DrugLabel:'].append(drugLabel)

    '''with open('publication.json', 'w') as fp:
        json.dump(dictionary, fp)'''
    return dictionary

def process(input_dicc,endpoint):
    sparql = SPARQLWrapper(endpoint)
    input_cui_uri = load_drug_cui(input_dicc)
    return get_publication(input_cui_uri, sparql)
