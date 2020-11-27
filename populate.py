from owlready2 import *
from pathlib import Path
import argparse
import re
from tqdm import tqdm

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

if args.no_basic:
    filepath = 'data/ontology/basic.txt'
    with open(filepath, 'w') as f:
        for n, c in tqdm(enumerate(list(onto.classes()))):
            print('c', c, type(c))
            # if c.subclasses():
            #     for c1 in list(c.subclasses()):
            #         print(c1, type(c1), end=' ')
            #     print()
            clsname = str(c).split('.')[1]
            insname = re.sub(r'(?<!^)(?=[A-Z])', '_', clsname).lower() # CameCase to snake_case
            i = onto[clsname](insname)
            print('i', i, type(i), i.name, i.iri)
            print('is', onto[clsname].instances())
            # a = c(clsname)
            # print('a', a, a.name, a.iri)

            print("\t<owl:NamedIndividual rdf:about=\"http://www.semanticweb.org/theorist/ontologies/2020/10/root-ontology#"+insname+"\">", file=f)
            print("\t\t<rdf:type rdf:resource=\"http://www.semanticweb.org/theorist/ontologies/2020/10/root-ontology#"+clsname+"\"/>", file=f)
            print("\t</owl:NamedIndividual>", file=f)
    # onto.save('data/ontology/temp.owl')