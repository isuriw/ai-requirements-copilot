# ReqPilot — Logical Data Model

## 1. Purpose

This document defines the logical data structure for ReqPilot, including entities, attributes, identifiers, relationships and data integrity rules.

It translates the concepts and behavioural requirements documented in the domain model and requirements document into a more precise data model.

The model remains independent of a specific database technology.

## 2. Modelling Principles

- Each entity has a clearly defined identity.
- Stable identities are separated from versioned information where historical changes must be preserved.
- Relationships explicitly identify the entities and versions they connect.
- Historical versions and relationships are preserved for traceability.
- AI-generated information retains its origin and supporting evidence where required.
- Human review is applied according to configured governance rules.
- The model should support AI evaluation and auditability without unnecessary complexity.

## 3. Model Status

This is a working model. Entity definitions and relationships will be refined as the design progresses.

## 4. Entities and Relationships

### 4.1 Requirement and Requirement Version

To be defined.

### 4.2 Task

**Purpose:** Represents the stable identity of a task throughout its lifecycle, independently of changes to its details.

**Attributes**

- **Task ID** — Unique, stable identifier for the task.
- **Created At** — Date and time the task was first created.
- **Created By** — Person or system responsible for initiating task creation.
- **Creation Origin** — Indicates whether the task originated from AI or a human.

**Identity and history rules**

- Task ID remains stable across all versions.
- Changes to task details are recorded through Task Version rather than by replacing the stable Task identity.
- The original AI-generated suggestion must remain recoverable after subsequent edits.

### 4.3 Task Version

**Purpose:** Stores a specific version of a task's details, preserving its history when changes occur.

**Attributes**

- **Task ID** — Identifies the parent Task.
- **Task Version** — Version number, unique within a Task.
- **Task Name** — Name of the task in this version.
- **Task Description** — Description of the task in this version.
- **Review Status** — Current review state of this specific version. Proposed values: Awaiting Review, Accepted and Rejected.
- **Work Status** — Progress of the task in this version. Proposed values: Not Started, In Progress and Completed.
- **Task Disposition** — Indicates whether the task remains active or is no longer required. Proposed values: Active, Cancelled and No Longer Required.
- **Priority** — Priority assigned to the task in this version.
- **Size** — Estimated task size.
- **Assigned To** — Person responsible for the task in this version.
- **Due Date** — Due date recorded for this version.
- **Version Created At** — Date and time this version was created.
- **Version Created By** — Person or system responsible for creating this version.
- **Change Summary** — Summary of the changes from the preceding version.
- **Disposition Reason** — Reason the task was cancelled or became no longer required, where applicable.

**Identity and history rules**

- The combination of Task ID and Task Version uniquely identifies a Task Version.
- Every edit creates a new Task Version; previous versions are preserved.
- The original AI-generated suggestion remains recoverable after subsequent edits.
- Routine administrative changes do not automatically require another review.
- Material changes are assessed under the configured governance rules.
- Review requirements are determined by the applicable governance rules. If review is required, the version awaits review. If review is not required, it may proceed under those rules.
- Human acceptance and automatic acceptance must remain distinguishable.
- When a task is cancelled or becomes no longer required, its history and previous versions are preserved.
- Cancellation or removal of the need for a task must not be recorded as successful completion.
- The reason for cancellation or the decision that the task is no longer required should be recorded.
- The exact rules for changing Task Disposition, including whether a new Task Version is required, remain to be finalised.

### 4.4 Task Review

**Purpose:** Records a review event for a specific Task Version, preserving who or what performed the review and the outcome.

**Attributes**

- **Task Review ID** — Unique identifier for the review event.
- **Task ID** — Identifies the parent Task.
- **Task Version** — Identifies the specific version reviewed.
- **Reviewer** — Person or system responsible for the review or automated governance decision.
- **Review Outcome** — Outcome recorded for the review, such as Accepted or Rejected.
- **Review Timestamp** — Date and time the review or decision occurred.
- **Review Notes** — Optional explanation or feedback.
- **Review Method** — Indicates whether the outcome came from a human review or an automated governance decision.

**Review rules**

- Each review event relates to a specific Task Version.
- Multiple review events may be recorded for the same version.
- Review history is preserved; a later review does not overwrite an earlier review.
- AI-generated tasks may initially have a Review Status of Awaiting Review.
- Review Outcome records an individual review decision.
- Task Version stores the current Review Status, while Task Review preserves the history of individual review events.
- Automated governance decisions must be distinguishable from human review decisions.

### 4.5 Task–Requirement Version Relationship

**Purpose:** Records which version of a task supports or implements which version of a requirement.

**Attributes**

- **Task ID** — Identifies the Task.
- **Task Version** — Identifies the specific Task Version.
- **Requirement ID** — Identifies the Requirement.
- **Requirement Version** — Identifies the specific Requirement Version.
- **Relationship Type** — Describes how the task relates to the requirement, for example Implements or Supports.

**Relationship rules**

- A Task Version may relate to multiple Requirement Versions.
- A Requirement Version may relate to multiple Task Versions.
- Historical relationships are preserved so the model can reconstruct which task version supported which requirement version at a given point in time.
- When a Requirement Version changes, linked tasks are assessed for impact.
- If the task's scope or intended outcome changes, a new Task Version is created and linked to the applicable Requirement Version. The previous Task Version and its historical relationships remain preserved.
- If the task remains valid and unchanged, the existing Task Version is retained and a new relationship is recorded to the new Requirement Version. The previous relationship remains available as historical evidence.
- Updating a relationship does not automatically create a new Task Version.
- Work Status must reflect actual progress and must not be assumed to carry forward without assessment.
- Any required review is determined by configured governance rules.

### 4.6 Other Entities

The following entities will be defined in subsequent modelling sessions:

- Decision and Decision Version
- Risk and Risk Version
- Approval
- Source
- Test Case
- Milestone
- Release

Additional review-related entities may be considered as the model develops, provided their responsibilities remain distinct from Task Review.

## 5. Confirmed Design Decisions

### 5.1 Current Review Status

- The current Review Status is stored on Task Version.
- Task Review is a separate entity that records individual review events.
- Review Status provides the current state of a version; Task Review preserves the detailed history.
- The model must distinguish human acceptance from automatic acceptance under governance rules.
- Governance rules determine whether a new Task Version requires review.
- A version that does not require review may proceed under the applicable governance rules.
- Consistency between the current Review Status, review history and governance decisions must be maintained.

### 5.2 Task Cancellation and Disposition

- Tasks are retained when cancelled or when they are no longer required; they are not deleted.
- Task history, previous versions and historical relationships are preserved.
- Cancellation and No Longer Required are distinct from successful completion.
- Task Disposition is modelled separately from Work Status.
- The reason for cancellation or the decision that the task is no longer required should be recorded.
- Exact transition rules and whether a disposition change requires a new Task Version remain to be refined.

## 6. Open Design Questions

- How should the model record the governance rule and decision that allowed a Task Version to proceed without human review?
- How will consistency between the current Review Status, review history and governance decisions be maintained?
- How should supporting source evidence be linked to AI-generated tasks and their review or governance decisions?
- What rules determine when a Task Disposition change requires a new Task Version?
- How should historical Task–Requirement Version relationships record their validity period or whether they remain current?

These questions will be refined as the model develops. They do not all need to be resolved before the first coding exercise.