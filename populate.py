from owlready2 import *
from pathlib import Path
import argparse
import re
from tqdm import tqdm
from paraphrase import get_synonyms_and_antonyms
from copy import deepcopy
import nltk
import string
# args
parser = argparse.ArgumentParser(description='Process options for KG individual population')
parser.add_argument('--no-basic', action='store_false', help='add basic individual derived from class name')
args = parser.parse_args()
print('args', args)

curpath = str(Path(__file__).resolve().parent)
onto_path.append("file://"+curpath+'/data/ontology/root-ontology.owl')
# onto = get_ontology("http://www.semanticweb.org/theorist/ontologies/2020/10/root-ontology").load()
onto = get_ontology("file://"+curpath+'/data/ontology/root-ontology.owl').load()
# print(onto, onto.classes(), list(onto.classes()))

is_noun = lambda pos: pos[:2] == 'NN'

if args.no_basic:
    filepath = 'data/ontology/basic.txt'
    filepath2 = 'data/ontology/paraphrase.txt'
    with open(filepath, 'w') as f, open(filepath2, 'w') as f2:
        for n, c in enumerate(list(onto.classes())):
            # print('c', c, type(c))
            # if c.subclasses():
            #     for c1 in list(c.subclasses()):
            #         print(c1, type(c1), end=' ')
            #     print()
            clsname = str(c).split('.')[1]
            insname = re.sub(r'(?<!^)(?=[A-Z])', '_', clsname).lower() # CameCase to snake_case
            sentence = insname.replace('_', ' ')
            tokenized = nltk.word_tokenize(sentence)
            postagged = nltk.pos_tag(tokenized)
            # wordlist = nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
            
            paraphrases = []
            for i, (word, pos) in enumerate(postagged):
                if not is_noun(pos):
                    continue
                cache = deepcopy(tokenized)
                synonyms, antonyms = get_synonyms_and_antonyms(word) 
                for j, synonym in enumerate(synonyms):
                    cache[i] = synonym
                    paraphrase = ' '.join(cache).translate(str.maketrans('', '', string.punctuation)).lower().replace(' ', '_')
                    print(clsname, insname, paraphrase)
                    paraphrases.append(paraphrase)
            # print('clsname', clsname, 'insname', insname)
            # i = onto[clsname](insname)
            # print('i', i, type(i), i.name, i.iri)
            # print('is', onto[clsname].instances())
            # print()
            # a = c(clsname)
            # print('a', a, a.name, a.iri)

            print("\t<owl:NamedIndividual rdf:about=\"http://www.semanticweb.org/theorist/ontologies/2020/10/root-ontology#"+insname+"\">", file=f)
            print("\t\t<rdf:type rdf:resource=\"http://www.semanticweb.org/theorist/ontologies/2020/10/root-ontology#"+clsname+"\"/>", file=f)
            print("\t</owl:NamedIndividual>", file=f)

            for paraphrase in paraphrases:
                print("\t<owl:NamedIndividual rdf:about=\"http://www.semanticweb.org/theorist/ontologies/2020/10/root-ontology#"+paraphrase+"\">", file=f2)
                print("\t\t<rdf:type rdf:resource=\"http://www.semanticweb.org/theorist/ontologies/2020/10/root-ontology#"+clsname+"\"/>", file=f2)
                print("\t</owl:NamedIndividual>", file=f2)
    # onto.save('data/ontology/temp.owl')