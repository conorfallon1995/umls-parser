from umlsparser import UMLSParser
import collections
umls = UMLSParser('/Users/conor/T/UMLSParser/umls-extract')

with open('icd10_unfiltered.csv', 'w') as f:
    f.write('icd9code;name;source;description\n')
    for cui, concept in umls.get_concepts().items():
        if 'ICD10CM' in concept.get_source_ids().keys():
            icd10ids = concept.get_source_ids().get('ICD10CM')
            name = concept.get_preferred_names_for_language('ENG')[0]
            for definition, source in concept.get_definitions():
                f.write(f'{icd10ids};"{name}";"{source}";"{definition}"\n')