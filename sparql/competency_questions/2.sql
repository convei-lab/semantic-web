PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lhi: <http://www.semanticweb.org/theorist/ontologies/2020/10/root-ontology#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?value ?individual WHERE { 
  ?class rdfs:subClassOf* lhi:8MonthOld .
  # sublclass restriciton
  ?class (rdfs:subClassOf)
   [
          a owl:Restriction ;
          owl:onProperty lhi:do ;
          (owl:someValuesFrom|owl:hasValue) ?value;
   ] .
  ?individual rdf:type ?value
}