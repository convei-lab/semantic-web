from owlready2 import *
from pathlib import Path
curpath = str(Path(__file__).resolve().parent)
onto = get_ontology("file://"+curpath+'/data/ontology/root-ontology.owl').load()
print(onto, onto.classes(), list(onto.classes()))