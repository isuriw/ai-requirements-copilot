# ReqPilot — Logical Model Progress

**Checkpoint:** 19 October 2026

## 1. Overall Progress

### Previously designed

The following entities and concepts have been designed at a conceptual level:

- Requirement and Requirement Version
- Source and traceability relationships
- Decision and Decision Version
- Approval
- Risk and Risk Version

These definitions and relationships will need to be checked against the detailed logical model as the design progresses.

### Current focus

- Task and Task Version
- Task Review
- Task–Requirement Version relationships
- Task cancellation and disposition

**Current status:** The core Task modelling decisions have been made and documented. The model is ready to support the first coding exercise, with some detailed rules left for later refinement.

### Next milestones

1. Begin Python implementation using a small meeting-note-to-task extraction example.
2. Test structured task extraction against expected results.
3. Introduce AI-based extraction and compare its output with the baseline.
4. Continue refining the logical model as implementation exposes important design questions.
5. Define Milestone, Release and Test Case entities.
6. Review the complete logical model against the requirements document, domain model and existing ADRs.
7. Develop the AI/ML design and evaluation dataset.

## 2. Modelling Principles

- Preserve historical versions and relationships.
- Keep entity identities independent where appropriate.
- Connect entities directly where relevant.
- Assess downstream impacts without assuming every related entity must change.
- Retain source evidence and provenance for AI-generated information where required.
- Apply review and approval according to configured governance rules.
- Support auditability and AI evaluation without unnecessary complexity.

## 3. Task and Task Version — Confirmed Decisions

### Task identity and versioning

- Task represents the stable identity of a task.
- Task Version stores the task details that can change over time.
- Every edit creates a new Task Version, preserving earlier versions.
- Task Name and Task Description are versioned.
- Assignment and Due Date are versioned because they can change.
- The original AI-generated suggestion must remain recoverable after edits.

### Proposed Task attributes

**Task**

- Task ID
- Created At
- Created By
- Creation Origin

**Task Version**

- Task ID
- Task Version
- Task Name
- Task Description
- Review Status
- Work Status
- Task Disposition
- Priority
- Size
- Assigned To
- Due Date
- Version Created At
- Version Created By
- Change Summary
- Disposition Reason, where applicable

These are working definitions and will be validated further as implementation progresses.

### AI-generated tasks and governance

- AI-generated tasks may initially have Review Status set to Awaiting Review.
- The original AI-generated suggestion must remain recoverable.
- Material changes to scope, intended outcome or meaning may require review.
- Routine administrative changes do not automatically reopen review.
- AI may assess change significance and confidence.
- Configured governance rules determine whether review is required.
- Human acceptance and automatic acceptance must remain distinguishable.
- A version that does not require review may proceed under the applicable governance rules.

### Separate status concepts

**Review Status** describes the current review state of a Task Version. Proposed values:

- Awaiting Review
- Accepted
- Rejected

**Work Status** describes actual progress. Proposed values:

- Not Started
- In Progress
- Completed

**Task Disposition** describes whether the task remains active or is no longer required. Proposed values:

- Active
- Cancelled
- No Longer Required

These concepts must remain distinct. In particular, cancellation must not be recorded as successful completion.

### Task cancellation and disposition

- Tasks are retained when cancelled or no longer required; they are not deleted.
- Previous versions, task history and historical relationships are preserved.
- The reason for cancellation or the decision that the task is no longer required should be recorded.
- Exact transition rules, including whether a disposition change requires a new Task Version, remain to be refined.

## 4. Task Review — Decision Confirmed

**Selected approach:** Model Task Review as a separate entity linked to a specific Task Version.

- Task Version stores the task details and current Review Status.
- Task Review records individual review events.
- Multiple review events may be recorded for the same Task Version.
- Review history is preserved rather than overwritten.
- Human review and automated governance decisions must be distinguishable.

**Proposed Task Review attributes**

- Task Review ID
- Task ID
- Task Version
- Reviewer
- Review Outcome
- Review Timestamp
- Review Notes
- Review Method

Proposed outcomes include Accepted and Rejected.

**Remaining refinement:** Determine how the current Review Status remains consistent with review history and automated governance decisions. This does not block the first coding exercise.

## 5. Task–Requirement Version Relationship

- The relationship identifies both Task ID + Task Version and Requirement ID + Requirement Version.
- Relationship Type describes the connection, for example Implements or Supports.
- A Task Version may relate to multiple Requirement Versions.
- A Requirement Version may relate to multiple Task Versions.
- Historical relationships must be preserved.
- A new Requirement Version triggers impact assessment but does not automatically create a new Task Version.
- If task scope or intended outcome changes, create a new Task Version and link it to the applicable Requirement Version.
- If the task remains valid and unchanged, retain the existing Task Version and record its relationship to the new Requirement