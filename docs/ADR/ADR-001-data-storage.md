# ADR-001: Data Storage Architecture

## Status

Accepted

## Context

ReqPilot needs to capture and manage information from a variety of
project sources, including Word documents, meeting transcripts,
emails, chat transcripts and other project artefacts.

The system needs to preserve the original source material while also
transforming relevant information into structured project knowledge
that can be searched, reviewed, approved and traced throughout the
project lifecycle.

The information ReqPilot needs to manage includes:

- Original project documents and artefacts
- Structured requirements
- Decisions
- Approvals
- Risks
- Test cases
- Stakeholders
- Relationships and traceability
- Additional requirement-specific information that may not fit
  predefined fields

A key requirement is that information must not be discarded simply
because it does not fit the initial requirements model.

The architecture therefore needs to balance:

- Preservation of original information
- Structured and reliable management of project knowledge
- Flexibility as requirements evolve
- Strong relationships and traceability

## Options Considered

### Option A — Relational Database

#### Pros

- Strong support for structured business entities
- Strong relationships between requirements, decisions, approvals,
  risks and test cases
- Reliable querying and reporting
- Well suited to maintaining traceability

#### Cons

- Requires careful data modelling to accommodate variations in
  requirements
- Excessive rigidity could increase schema evolution effort
- Flexible requirement information requires additional design
  consideration

---

### Option B — Document Database

#### Pros

- Flexible structure for information that varies between requirements
- Easy to evolve as new information types are identified
- Well suited to storing semi-structured information

#### Cons

- Complex relationships between requirements, approvals, decisions,
  risks and test cases may be harder to enforce and query consistently
- Governance and reporting across related entities may become more
  difficult
- Maintaining reliable end-to-end traceability may require additional
  application logic

---

### Option C — Combined Storage Architecture

Use separate storage approaches for original project artefacts and
structured project knowledge.

#### Pros

- Original source artefacts can be preserved without forcing them
  into a structured data model
- Structured project knowledge can be stored in a form optimised
  for relationships, querying and reporting
- Requirement information can support flexible additional attributes
  without requiring the core model to change for every new type of
  information
- Supports end-to-end traceability between requirements and their
  original sources

#### Cons

- Multiple storage technologies increase operational complexity
- Additional integration and reference management is required
- Monitoring, backup and recovery become more complex
- Potentially higher infrastructure and maintenance costs

## Decision

**Option C — Combined Storage Architecture**

ReqPilot will use separate storage approaches for:

1. Original project artefacts and source material
2. Structured project knowledge and relationships

The specific technologies used for each storage layer will be
determined through subsequent architecture decisions.

## Rationale

The combined storage architecture provides the best balance between
structure, flexibility and preservation for ReqPilot's requirements
management use case.

### Preserve original artefacts

Original project documents, transcripts, emails and other source
material must be retained as evidence.

This ensures that extracted requirements can always be traced back to
their original context and allows users to review the source material
when requirements are challenged or require clarification.

### Structured, queryable project knowledge

Requirements, decisions, approvals, risks, test cases and
stakeholders represent structured business entities with important
relationships.

These relationships need to support reliable searching, reporting,
approval processes and end-to-end traceability.

### Flexible requirement information

Not all useful information extracted from a requirement will
necessarily fit into predefined fields.

The structured repository must therefore support additional
requirement-specific information without requiring the core data
model to be redesigned whenever a new type of information is
identified.

### Traceability

Requirements must retain links to the source material from which they
were derived.

For example:

    Source Document
          |
          v
    Requirement
          |
      +---+---+
      |       |
      v       v
    Decision Approval
      |
      v
    Test Case

This supports auditability, impact analysis and stakeholder
confidence in the requirements repository.

## Consequences

### Benefits

- Original source artefacts are preserved.
- Structured project knowledge can be searched and queried reliably.
- Relationships between requirements and related project entities
  can be explicitly maintained.
- Requirements can retain relevant information that does not fit
  predefined fields.
- Requirements can be traced back to their original evidence.
- The architecture can evolve without requiring the original source
  material to be restructured.

### Trade-offs

- Multiple storage mechanisms increase implementation and operational
  complexity.
- Additional integration logic may be required between source
  artefacts and structured project knowledge.
- References between storage layers must be maintained reliably.
- Monitoring, backup and recovery processes are more involved.
- Infrastructure and maintenance costs may be higher than using a
  single storage mechanism.

## Design Principles

- Original source artefacts must be preserved.
- Structured project knowledge should be searchable and traceable.
- Requirements should support flexible additional information.
- Information should not be discarded simply because it does not fit
  a predefined field.
- AI-generated information must remain distinguishable from
  business-approved information.
- Every approved requirement should be traceable to its supporting
  evidence.
- Specific technology choices should be made through separate
  architecture decisions.