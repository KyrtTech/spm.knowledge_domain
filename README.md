#  Service Package Manager - Knowledge Domain

## What

SPM Knowledge Domain defines a technology-independent, RDF-based vocabulary and ontology for:
- describing software services
    - their dependencies (usually other software services)
    - minimum and recommended resource requirements
- describing infrastructure providers and services
    - a common way of describing similar services between different providers
- describe and discover strategies for installing software services on different infrastructure environments


SPM leverages existing automation technologies (`Terraform`, `Pulumi`, `AWS CDK`, any other) for deployment by finding appropriate **install strategies**.

SPM does not replace infrastructure automation tools; it complements them:
- deployment orchestrator
- deployment strategy discovery
- it relies on existing infra tech for best practices and reproducible results

## How
A foundational project under `SPM` is defining the `vocabulary`, `taxonomies` and `ontologies` that are being used by other projects.

There are a few reasons why this is useful:

* have a common vocabulary when referring to different parts of a service
    * infra req
    * inputs
    * outputs
    * file formats
    * dependencies on other services
* ability to check for compatibilities between services
    * having a `taxonomy` can greatly help with checking if different `systems` are compatible
    * this also applies to checking if an `infra provider` is compatible with a `system`
* suggest different services based on needs
    * deploying a DB using a dedicated server or using a managed service for instance
    * switch to a different vendor for a Message Broker
* tooling around `service discovery`, `service integration` and `service deployment`

## Structure

###  Ontology
Most files related to describing the `vocabulary` and `ontology` are stored under `ontology` folder.

Most of the files are using `rdf` to describe the different `classes` and `properties`, but you may also encounter `json-ld` and `html` files.

### Docs
Documentation will reside under the `docs` folder. This will discuss at length the different concepts used in this knowledge domain.

### Examples

Under `/examples` you can see examples. Examples are using multiple formats
- html
- [turtle](https://www.w3.org/TR/turtle/)
- [json-ld](https://json-ld.org/)

We try to provide as many examples as possible.

## File Format
We are using `.ttl` (turtle) files for vocabulary and ontology. 

### JSON-LD
You may also encounter `json-ld` files. The main rationale about using this is that other projects in the `spm` effort will expose API that use `json` as the protocol. Adding a context to a JSON file should be enough to provide data linking and allow for more richer and in depth analysis.

## 3rd Party Vocabularies and Ontologies

We rely on existing and widely used and accepted `vocabularies` and `ontologies` where this seems to be appropriate.

This is a growing list of external resources that are used across this project.

### Dublin Core

Dublin Core is one of the main source for the vocabularies and ontologies we are using.

More precisely we are using the following namespaces
- http://purl.org/dc/elements/1.1/
- http://purl.org/dc/terms/
- http://purl.org/dc/dcmitype/

> Note: there are classes and properties that we aren't using from these namespaces.

### Schema.org

Where appropriate we use the vocabulary provided by [schema.org](https://schema.org/).

Where SEO is a goal schema.org is preferred, most likely in conjunction with [microdata](https://developer.mozilla.org/en-US/docs/Web/HTML/Microdata).

### FriendOfAFriend (foaf)

When describing creators, contributors or persons of interesest we mostly rely on [FoaF vocab](http://xmlns.com/foaf/spec/).

### DataCatalogVocabulary (DCAT) - v3
We aren't using DCAT actively at this point, but this is a good resource if you ever need to describe a `data catalog`.

V3 recommendation can be found [here](https://www.w3.org/TR/vocab-dcat-3/).


> Note: this list is a living list and we may add other 3rd party vocabularies to it. 

## License

This project is licensed under the [Apache License, Version 2.0](LICENSE).

Third-party vocabularies and ontologies referenced above remain under their own licenses.
