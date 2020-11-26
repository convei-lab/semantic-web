# semantic-web
This repo serves a pipelined tutorial that aims to build up a knowledge base from text files that are web-crawled with Protege and Apache Jena.

## Prerequisite
1. [Protege](https://protege.stanford.edu/)
2. [Apache Jena](https://jena.apache.org/download/index.cgi)
3. [Apache Jena Fuseki](https://jena.apache.org/download/index.cgi)

Check [this link](https://www.youtube.com/watch?reload=9&v=8F3TWJvgmBU) for installing Apache Jena & Fuseki (in Korean).

## Installation

0. Install python dependencies.
```
pip install -r requirements.txt
```
1. Web scrap. (results in /data/raw)
```
python scrap.py
```
2. Explore scrapped data. (Results in ./data/stat)
```
python stat.py
```
3. Translate into Korean. (Optional. Results in ./data/translated)
```
python translate.py #/data/translated
```
4. Annotate the dataset. Insert any class label of your interest as a text span wrapped with doulbe squared bracket, e.g. [[Fruit]]. Also, correct the chunking of paragraphs, incorrect newlines charaters, and etc.
```
mkdir ./data/anno
cp -r ./data/raw/* ./data/anno
* Annotation with data/anno
```
5. Create a neat exel file for annotation. (Optional)
```
python anno2xls.py
```

6. Create OWL object classes & properties (T-Box) with Protege and place it under ./data/ontology. You can  use a [WebProtege](https://webprotege.stanford.edu/) to collaborate with your team.

    * ./data/ontology/root-ontology.owl

7. Populate individuls.
```
python populate.py
```
8. Save root-ontology.owl as a turtle syntax.

    * ./data/ontology/root-ontology.ttl

9. Run Apache Jena Fuseki.