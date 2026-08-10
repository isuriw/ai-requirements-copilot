# Domain Model

## Core Entities

### Requirement

Represents a business requirement that has been captured, reviewed,
approved and maintained throughout the project lifecycle.

#### Identity

- Requirement ID
- Title
- Description

#### Classification

- Requirement Type
- Priority
- Status

#### Ownership

- Business Owner
- Business Analyst
- Technical Owner

#### Lifecycle

- Version
- Created Date
- Last Updated
- Approval Status
- Approved By
- Approval Date

#### Traceability

- Source Documents
- Related Decisions
- Related Requirements
- Related User Stories
- Related Test Cases
- Related Risks


### Document

Represents a source of project information.

Properties

- Document ID
- Name
- Type
- Version
- Upload Date
- Author


### Decision

Represents a project decision.

Properties

- Decision ID
- Description
- Decision Maker
- Decision Date
- Reason
- Supporting Evidence


### Stakeholder

Represents a project stakeholder.

Properties

- Stakeholder ID
- Name
- Role
- Team
- Email


### Test Case

Represents a test case linked to one or more requirements.

Properties

- Test Case ID
- Name
- Status
- Owner


### Risk

Represents a project risk.

Properties

- Risk ID
- Description
- Owner
- Severity
- Status


### Approval

Represents a formal decision by an authorised stakeholder
to approve, reject or request changes to a requirement.

Properties

- Approval ID
- Requirement ID
- Requirement Version
- Approver
- Decision
- Date
- Comments


# Relationships

- A Document can contain many Requirements.
- A Requirement can originate from many Documents.
- A Requirement can have many Decisions.
- A Requirement can have many Approvals.
- A Requirement can have many Test Cases.
- A Requirement can have many Risks.
- A Decision can reference many Documents.
- A Stakeholder can own many Requirements.
- A Stakeholder can provide many Approvals.
- Each Approval relates to a specific Requirement version.