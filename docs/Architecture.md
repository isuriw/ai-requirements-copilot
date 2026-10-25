# High-Level Architecture

## Purpose

This document describes the high-level components of ReqPilot
and how information flows through the system.

## Initial Concept

```text
                    ┌──────────────────────┐
                    │       Users          │
                    │ BA / Business /      │
                    │ Engineers / Testers  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     ReqPilot UI      │
                    │                      │
                    │ Upload / Search /    │
                    │ Review / Approve     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Knowledge Ingestion │
                    │                      │
                    │ Documents            │
                    │ Meetings             │
                    │ Emails               │
                    │ Chat                 │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     AI Analysis      │
                    │                      │
                    │ Extract              │
                    │ Classify             │
                    │ Detect duplicates    │
                    │ Identify conflicts   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Requirements        │
                    │ Repository           │
                    │                      │
                    │ Requirements         │
                    │ Decisions            │
                    │ Approvals            │
                    │ Risks                │
                    │ Traceability         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Delivery Outputs     │
                    │                      │
                    │ Requirements         │
                    │ Test Cases           │
                    │ Decisions            │
                    │ Reports              │
                    └──────────────────────┘