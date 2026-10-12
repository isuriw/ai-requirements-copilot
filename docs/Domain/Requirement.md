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


### Test Case

A Test Case validates a specific Requirement Version.

A Requirement Version can have multiple Test Cases.

A Test Case should not automatically transfer to a new Requirement
Version when the Requirement changes.

A new or updated Requirement Version should be assessed to determine
whether new or modified Test Cases are required.

The Requirement ↔ Test Case relationship should contain:

- Requirement ID
- Requirement Version
- Test Case ID
- Relationship ID


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


Impact Analysis

A change to a Requirement Version may affect other entities and relationships within the project knowledge model.

When a new Requirement Version is created, ReqPilot should assess the relationships associated with the previous version and identify potential impacts on related entities, including Decisions, Risks, Tasks, Milestones, Releases, and Test Cases.

Impact analysis should be transitive. If an affected entity has relationships with other entities, those relationships should also be assessed for potential impact. Analysis continues until no additional potentially affected entities are identified.

The impact analysis must:

Preserve the history of the previous Requirement Version and its relationships.
Determine whether existing relationships remain valid, need modification, or should be removed.
Identify new relationships that may need to be created.
Avoid assuming that every related entity is affected; each relationship must be assessed.
Detect and prevent circular traversal by tracking entities that have already been evaluated.

The resulting impact assessment should identify the potentially affected entities and provide sufficient context for review or further processing.

## Requirement Decomposition

When a requirement is determined to be too broad or complex and needs to be broken into multiple independent requirements, the resulting items are created as **new Requirement identities** rather than additional versions of the original requirement.

The original requirement is retained for historical traceability and its status is changed to **Closed**, with the reason recorded as decomposition.

The new requirements should maintain a relationship to the original requirement so that ReqPilot can trace how they were derived.

Requirement versioning and requirement decomposition are distinct concepts:

* **Versioning** represents a change to the definition of the same requirement.
* **Decomposition** creates new requirements from an existing requirement.


## Task

A Task represents a unit of work required to deliver or support project outcomes.

### Core Attributes

- Task ID
- Task Name
- Task Description
- Status
- Priority
- Size
- Created Date
- Created By
- Assigned To
- Due Date

Created By and Assigned To represent different roles. The person who creates a task may not be the person responsible for completing it.

### Task–Requirement Version Relationship

Tasks are linked to specific Requirement Versions through a separate relationship.

The relationship contains:

- Task ID
- Requirement ID
- Requirement Version
- Relationship Type

Examples of Relationship Types include Implements and Supports.

A Task can support multiple Requirement Versions, and a Requirement Version can be supported by multiple Tasks.

### Change and Traceability

When a new Requirement Version is created, existing Task–Requirement Version relationships must be preserved.

ReqPilot should assess whether each existing task remains relevant, requires modification, or needs additional work for the new Requirement Version.

New relationships should be created when appropriate. Historical relationships must not be overwritten, and a new task must not be created automatically for every new Requirement Version.

Task status is independent of Requirement status. Completing a task does not automatically mean that the associated requirement has been verified.

### AI-Generated Task Handling

ReqPilot may create a Task directly from an AI-generated suggestion.

AI-generated Tasks must be distinguishable from human-created Tasks and must initially be marked as awaiting review.

The Task should retain:
- Creation origin (AI or Human)
- AI generation timestamp, where applicable
- Review status
- Supporting source and Requirement Version relationships

An AI-generated Task awaiting review must not be treated as accepted work. An authorised user can accept, edit, or reject the task.

The review outcome and reviewer should be recorded for traceability. Rejecting a Task must not delete the supporting source evidence or the history of the AI-generated suggestion.

### Review and Modification

An authorised reviewer can:

- **Accept** the Task as proposed.
- **Edit** the Task before accepting it.
- **Reject** the Task if it is not required or is incorrect.

ReqPilot must preserve the Task's AI-generated origin when it is edited by a human.

The system must record the review outcome, reviewer, and review timestamp. Where a reviewer edits the Task, the changes should be traceable so that the original AI suggestion can be distinguished from the human-modified result.

Rejecting a Task must preserve its history and supporting source evidence.