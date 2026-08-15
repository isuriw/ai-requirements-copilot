# ADR-002: Flexible Requirement Data

## Status

Accepted

## Context

Business requirements can contain different types of information
that may not fit into the core Requirement data model.

ReqPilot needs to retain this information without requiring changes
to the core data model whenever a new type of information is
identified.

At the same time, flexible information must remain sufficiently
structured to support querying, validation and future analysis.

The solution therefore needs to balance flexibility with data
quality and usability.


## Options Considered

### Option A — Flexible Attributes

Pros:

- Easy to implement
- Flexible for varying requirements
- New attributes can be added without changing the core data model
- Business rules can evolve without requiring changes to the core
  schema

Cons:

- Data can become inconsistent without appropriate governance
- Incorrect or inconsistent attribute names and data types may make
  querying more difficult
- Additional validation and guardrails are required

### Option B — Entity-Attribute-Value

Pros:

- Highly flexible mechanism for representing custom attributes
- Provides a consistent structure for storing attribute definitions
  and values

Cons:

- More complicated to build and maintain
- Queries across multiple attributes can become complex
- Additional application logic may be required for validation
- Changes to attribute definitions may have a wider impact

### Option C — Unstructured Additional Information

Pros:

- Easy to implement
- Flexible for AI extraction
- Can retain information without predefined fields

Cons:

- Information cannot be reliably queried as structured data
- Additional interpretation is required to extract structured
  information
- Data quality and consistency are difficult to enforce

## Decision

We will use Option A — Flexible Attributes.

The core Requirement model will contain attributes that are common
across requirements. Additional requirement-specific information
will be stored as custom attributes.

Custom attributes will be subject to application-level guardrails
to maintain consistency while retaining flexibility.

## Rationale


Flexible attributes provide the best balance between flexibility,
simplicity and queryability for ReqPilot.

The core Requirement model will contain attributes that are common across requirements.

Additional information will be stored as custom attributes with application-level guardrails to maintain consistency.

This allows ReqPilot to retain useful information without requiring changes to the core data model whenever new requirement attributes
are identified.

Flexible attributes were preferred over Entity-Attribute-Value because
they provide the required flexibility without introducing the additional
querying and implementation complexity associated with an EAV model.

Application-level guardrails will provide sufficient structure and
validation for the initial implementation.

## Consequences

### Benefits

- Easy implementation
- Flexible requirement model
- Queryable custom information
- Reduced need for core schema changes
- Ability to retain information that does not fit the base model

### Trade-offs

- Additional validation and governance are required
- Poorly governed attributes could become difficult to query
- The application must provide appropriate guardrails



## Design Principles

- Custom attributes should have a defined name and description.
- Common custom attributes should use standardised names.
- Custom attributes should have defined or recommended data types.
- Attribute values should be validated where practical.
- Equivalent attributes should not be created under different names.
- Frequently used or business-critical custom attributes should be
  candidates for promotion into the core domain model.
- Original source information should be retained even when it cannot
  be mapped to a custom attribute.
- AI-generated attribute values must retain their provenance and
  verification status.
- AI-generated information must not automatically be treated as
  business-approved information.

  - Human verification should be proportional to the importance and
  risk of the information rather than being required for every
  AI-generated value.
- High-confidence, low-risk values may be automatically accepted.
- Important or business-critical attributes should require human
  verification regardless of AI confidence.
- New custom attributes proposed by AI should require human
  verification before being added to the approved attribute set.
- AI confidence thresholds should be configurable rather than
  hard-coded.