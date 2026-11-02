#!/usr/bin/env python3
"""Validate the Turtle files under ontology/.

Checks:
  * every file parses;
  * properties declared owl:FunctionalProperty have at most one value per subject;
  * values of functional properties carry no language tag (they are data, not text);
  * literals typed with the XSD namespace use a datatype that XSD defines.

Exits with status 1 when any check fails.
"""

import sys
from collections import defaultdict
from pathlib import Path

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import OWL, RDF, XSD

ONTOLOGY_DIR = Path(__file__).resolve().parent.parent / "ontology"

XSD_DATATYPES = {
    "string", "boolean", "decimal", "integer", "double", "float", "date", "dateTime",
    "time", "duration", "anyURI", "long", "int", "short", "byte", "nonNegativeInteger",
    "positiveInteger", "nonPositiveInteger", "negativeInteger", "unsignedLong",
    "unsignedInt", "unsignedShort", "unsignedByte", "gYear", "gYearMonth", "gMonth",
    "gMonthDay", "gDay", "hexBinary", "base64Binary", "normalizedString", "token",
    "language", "Name", "NCName", "NMTOKEN", "QName",
}


def load(errors):
    graph = Graph()
    for path in sorted(ONTOLOGY_DIR.rglob("*.ttl")):
        try:
            graph.parse(path, format="turtle")
        except Exception as e:
            errors.append(f"{path.relative_to(ONTOLOGY_DIR)}: parse error: {e}")
    return graph


def check_functional(graph, errors):
    for prop in sorted(set(graph.subjects(RDF.type, OWL.FunctionalProperty))):
        values = defaultdict(list)
        for subject, value in graph.subject_objects(prop):
            values[subject].append(value)
            if isinstance(value, Literal) and value.language:
                errors.append(
                    f"{subject}: {prop} is single-valued data but has language tag @{value.language}: {value!r}"
                )
        for subject, vals in values.items():
            if len(vals) > 1:
                errors.append(
                    f"{subject}: {prop} allows one value but has {len(vals)}: {', '.join(map(str, vals))}"
                )


def check_datatypes(graph, errors):
    seen = set()
    for subject, prop, value in graph:
        if not isinstance(value, Literal) or value.datatype is None:
            continue
        datatype = str(value.datatype)
        if not datatype.startswith(str(XSD)):
            continue
        name = datatype[len(str(XSD)):]
        if name not in XSD_DATATYPES and (subject, prop) not in seen:
            seen.add((subject, prop))
            errors.append(f"{subject}: {prop} uses unknown datatype xsd:{name}")


def main():
    errors = []
    graph = load(errors)
    check_functional(graph, errors)
    check_datatypes(graph, errors)

    if errors:
        print(f"{len(errors)} problem(s) found:")
        for error in errors:
            print(f"  - {error}")
        return 1

    functional = len(set(graph.subjects(RDF.type, OWL.FunctionalProperty)))
    print(f"OK: {len(graph)} triples, {functional} single-valued properties checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
