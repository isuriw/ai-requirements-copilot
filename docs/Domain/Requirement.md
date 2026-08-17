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

## Modelling Decisions

- Requirement ID: need to be unique id that doesn't change with requiremnet modifications
- Owner: entity that the requirement can have a relationship to. That can change during the lifetime of the project
- Version: need to have lines for each version
- Source artefacts: relationship to seperate data source
- Reviewed By: goes into seperate relationship table
- Accepted By: same as above
- Jira Feature ID: seperate relationship
- Provenance: maintained primarily at Requirement Version level,   with detailed attribute-level provenance where required.