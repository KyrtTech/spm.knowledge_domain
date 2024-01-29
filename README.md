#  Service Package Manager - Knowledge Domain

A foundational project unde `SPM` is defining the `taxonomies` and `ontologies` that are being used by other projects.

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
* tooling around `service discovery`, `service integration` and `service deployment`

## Structure

Taxonomies are found under `taxonomies` folder.

Ontologies are found under `ontologies` folder.

## File Format
At the moment we're using [TOML](https://toml.io/en/) as our file format for both `taxonomies` and `ontologies`.

This may change in the future. One possible direction is to develop a simple language for this and implement tooling around it.