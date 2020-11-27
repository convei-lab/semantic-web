PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lhi: <http://www.semanticweb.org/theorist/ontologies/2020/10/root-ontology#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?class ?property ?value WHERE { 
  ?class rdfs:subClassOf* lhi:8MonthOld .
  # sublclass restriciton
  ?class (rdfs:subClassOf)
   [
          a owl:Restriction ;
          owl:onProperty ?property ;
          (owl:someValuesFrom|owl:hasValue) ?value
   ] .
}

-- PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
-- PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
-- PREFIX lhi: <http://www.semanticweb.org/theorist/ontologies/2020/10/root-ontology#>
-- PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
-- PREFIX owl: <http://www.w3.org/2002/07/owl#>

-- SELECT ?class ?property ?value WHERE { 
-- #  ?s rdfs:subClassOf* lhi:Toddler
  
-- #  {?s rdf:type lhi:10MonthOldBoy}
-- #  UNION
-- #  {?s rdf:type lhi:10MonthOldGirl}
  
-- #  ?s lhi:hasAge xsd:nonNegativeInteger
  
--   ?class rdfs:subClassOf* lhi:8MonthOld .
-- #  ?class (rdfs:subClassOf|owl:equivalentClass)/owl:onProperty ?property.
  
-- #sublclass restriciton
--   ?class (rdfs:subClassOf)
--    [
--           a owl:Restriction ;
--           owl:onProperty ?property ;
--           (owl:someValuesFrom|owl:hasValue) ?value
--    ] .
  
-- #  ?restriction (rdfs:subClassOf|(owl:intersectionOf/rdf:rest*/rdf:first))* ?ingredient1.
-- #  ?ingredient1 owl:someValuesFrom :ImprovingDistanceVision.
  
-- #  FILTER NOT EXISTS {?s lhi:hasAge xsd:nonNegativeInteger}
-- }