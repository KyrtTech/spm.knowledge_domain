#  Service Package Manager - Knowledge Domain

A foundational project unde `SPM` is defining the `vocabulary`, `taxonomies` and `ontologies` that are being used by other projects.

There are a few reasons why this is useful:

* have a common vocabulary when refering to different parts of a service
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
Documentation will reside under the `doc` folder. This will discuss at length the different concepts used in this knowledge domain.

### Examples

Under `/example` you can see examples. Examples are using multiple formats
- html
- [turtle](https://www.w3.org/TR/turtle/)
- [json-ld](https://json-ld.org/)

We try to provide as many examples as possible.

## File Format
We are using `.ttl` (turtle) files for vocabulary and ontology. 

### JSON-LD
You may also encounter `json-ld` files. The main rationale about using this is that other projects in the `spm` effort will expose API that use `json` as the protocol. Adding a context to a JSON file should be enough to provide data linking and allow for more richer and in depth analysis.