from rdflib import Graph, URIRef, Namespace, Literal
from rdflib.namespace import RDF, XSD

# Load your RDF file
g = Graph()
g.parse("AirBnb2024-csv.rdf", format="xml")

# Define the namespace and property
SCHEMA = Namespace("https://schema.org/")
price_property = URIRef("https://schema.org/price")

# Iterate over each price entry, modify and replace it with an integer value
for s, p, o in g.triples((None, price_property, None)):
    # Check if it's a price with type XSD.int or XSD.float
    if o.datatype in [XSD.int, XSD.float]:
        # Convert the value to an integer after removing commas
        try:
            price_value = int(float(str(o).replace(",", "")))
            # Replace the old price value with the new integer value
            g.set((s, p, Literal(price_value, datatype=XSD.int)))
        except ValueError as e:
            print(f"Skipping value '{o}' due to error: {e}")

# Save the modified graph to a new file
g.serialize("modified_file.rdf", format="xml")
