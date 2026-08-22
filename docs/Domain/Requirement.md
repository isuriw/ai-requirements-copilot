# Requirement

## Purpose

## Core Attributes

- Requirement ID
- Title
- Description
- Type
- Priority
- Status
- Owner
- Current Version
- Created At
- Last Modified At

## Custom Attributes

- Project-specific attributes
- AI-discovered attributes
- Validated according to ADR-002

## Provenance

Provenance will primarily be maintained at the Requirement Version level.

Each Requirement Version will retain information about the source and creation context.

Detailed attribute-level provenance will only be maintained where required, such as for AI-derived, business-critical or low-confidence information.

This avoids unnecessary complexity while maintaining sufficient traceability for important information and AI-generated decisions.

## Lifecycle

## Relationships

- Owner → Person/Stakeholder
- Sources → Source Artefacts
- Approvals → Approval
- Reviews → Review
- Decisions → Decision
- Risks → Risk
- Test Cases → Test Case
- Tasks/Milestones → Delivery Planning
- External References → External Systems

### Decision

A Decision records a business or project choice that establishes,
changes or constrains how one or more requirements should be
interpreted or implemented.

A Decision can affect multiple Requirements.

A Decision has its own immutable ID and maintains version history.

Core information:

- Decision ID
- Decision Statement
- Decider
- Source
- Source Location
- AI Confidence
- Version

Decisions can be associated with multiple Requirements.

### Approval
Approval
├── Approval ID
├── Requirement ID
├── Requirement Version
├── Approver / Approval Actor
├── Approval Method
├── Approval Status
├── Approval Timestamp
└── Approver Notes
 
### Risk

A Risk represents a potential event, condition or circumstance that
could negatively affect project or business outcomes and requires
assessment or management.

A Risk has its own immutable ID and maintains version history.

Initial Risk Types:
- Financial
- Operational
- Data
- Compliance

A Risk can exist independently of a Requirement.

Core information:
- Risk ID
- Risk Name
- Risk Domain
- Risk Type
- Risk Owner
- Risk Version
- Risk Assessment
- Legislative References where applicable

Risk ↔ Requirement is a many-to-many relationship.

The relationship should identify:
- Requirement ID
- Requirement Version
- Risk ID
- Risk Version
- Relationship ID
- Relationship Type

Examples of Relationship Types:
- Causes
- Resulting From
- Mitigates
- Contributes To


## Modelling Decisions

- Requirement ID: need to be unique id that doesn't change with requiremnet modifications
- Owner: entity that the requirement can have a relationship to. That can change during the lifetime of the project
- Version: need to have lines for each version
- Source artefacts: relationship to seperate data source
- Reviewed By: goes into seperate relationship table
- Accepted By: same as above
- Jira Feature ID: seperate relationship
- Provenance: maintained primarily at Requirement Version level,   with detailed attribute-level provenance where required.

## Lifecycle

A requirement progresses through a defined lifecycle from initial
capture through to verification.

- A requirement initially captured by ReqPilot has a status of
  Received.
- A requirement can progress through Draft, Proposed, Approved,
  Implemented and Verified states.
- A proposed requirement can be Rejected.
- An approved requirement can become Superseded.
- Requirement IDs remain unchanged when requirements are modified.
- Each significant modification creates a new Requirement Version.
- Material changes require human approval.
- AI can assess whether a change is minor or material and provide
  a confidence score.
- AI assessment is advisory and does not independently determine
  approval requirements.
- High-confidence minor changes may be automatically approved when
  configured business rules allow this.
- Auto-Approved changes must remain distinguishable from
  human-approved changes.


