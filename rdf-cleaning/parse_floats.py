from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import XSD

# Load RDF Graph
g = Graph()
g.parse("modified_file.rdf", format="xml")

# Define the namespace and property
SCHEMA = Namespace("https://schema.org/")
longitude_property = URIRef("https://schema.org/longitude")

# Correct any improperly typed longitude values
for s, p, o in g.triples((None, longitude_property, None)):
    if not isinstance(o.value, float):
        # Convert value to xsd:float explicitly
        try:
            corrected_longitude = Literal(float(o), datatype=XSD.float)
            g.set((s, p, corrected_longitude))
        except ValueError as e:
            print(f"Could not convert {o} to float: {e}")

# Save the modified RDF file
g.serialize("corrected_file.rdf", format="xml")
