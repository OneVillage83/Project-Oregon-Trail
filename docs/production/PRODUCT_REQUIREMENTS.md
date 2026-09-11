# Product requirements and acceptance boundaries

Version 0.2 | Specification | Product owner: project maintainer

## Authority of requirements

Inherited requirements below come from the original foundation and the visible concept discussion. Working defaults are implementation assumptions that must be recorded as decisions, not retroactively described as earlier user approvals. Exact historical setting, final title, content rating, launch era ceiling, hardware minimums, funding, and price remain open.

## Requirement register

| ID | Required capability | Acceptance evidence |
|---|---|---|
| PR-001 | Simulation alone owns authoritative state and outcomes | Injected outcome claims cannot mutate a world |
| PR-002 | Complete baseline play without external servers or per-command fees | Offline install/start/play/save/reload test |
| PR-003 | Free-form language is a primary interaction path | Held-out command interpretation and human playtest |
| PR-004 | Efficient menus and visual selection coexist with language | Menu and text produce equivalent normalized intents |
| PR-005 | Perception Mode uses observer skills, attention, and conditions | Different observers see different justified details |
| PR-006 | Skills and social identity emerge through meaningful practice | Hunter-to-investigator progression without class switch |
| PR-007 | Seeded geography and committed relevant truth precede discovery | Exploration order does not rewrite established facts |
| PR-008 | Consequential changes and entity identities persist | Return-to-location and reload fixtures |
| PR-009 | Evidence follows actual events, not generated narrative answers | Case provenance reconstructs cause and traces |
| PR-010 | Reputation, rumors, and knowledge travel through channels | No distant knowledge before delivery |
| PR-011 | Production, logistics, ownership, supply, and demand interact | Road disruption affects real deliveries and stock |
| PR-012 | Creative engineering uses reusable properties and processes | Distinct improvised solutions without bespoke verbs |
| PR-013 | Health, nutrition, injuries, disease, and care are world systems | Exposure-to-symptom-to-care causal tests |
| PR-014 | Ecology, weather, terrain, and resources affect decisions | Weather and depletion change routes and supply |
| PR-015 | NPCs have knowledge, goals, relationships, and limited authority | NPC action uses shared rules and respects permissions |
| PR-016 | Conflict, crime, investigation, and law have consequences | Force and accusation do not bypass evidence or ownership |
| PR-017 | Institutions, governance, employment, education, and organizations exist | Budgeted policy and teaching affect world capability |
| PR-018 | Real technological adoption changes mechanics and visuals through later eras | Prerequisite-gated industry, vehicles, modern materials |
| PR-019 | Families, institutions, places, and history support generational continuity | Death/retirement/continuation preserves ownership and history |
| PR-020 | Modular 2D presentation reflects real state and direction | State/asset and spatial consistency tests |
| PR-021 | Mobile remains feasible without silently changing world mechanics | Early device build and cross-platform fixtures |
| PR-022 | Saves are versioned, recoverable, and support bounded exact replay | Crash, migration, and replay qualification |
| PR-023 | Models and runtimes are replaceable; grammar is not semantic proof | Identical accepted intent produces identical simulation result |
| PR-024 | Consequential actions are explainable and traceable | Input-to-event trace with private/public separation |
| PR-025 | Every meaningful change has append-only UTC history | Existing history validator and changed-path coverage |
| PR-026 | Accessibility, localization, and onboarding are architectural concerns | Keyboard/touch/readability and no-leak accessible views |
| PR-027 | Content is validated, versioned, authorable, and attributable | Content compiler rejects invalid dependencies and assets |
| PR-028 | Distribution is honest, licensed, recoverable, and supportable | Release manifest, notices, rollback, and scope review |
| PR-029 | Gemma 4 is prioritized for evaluation, not assumed to beat all alternatives | Recorded device-specific model qualification |
| PR-030 | World scale uses explicit fidelity policies with continuity invariants | Promotion/demotion and cross-boundary accounting tests |
| PR-031 | Time advancement is controllable and supports long campaigns | Interruptible standing orders and succession playtests |
| PR-032 | Quality gates require actual results, not documents alone | Scenario, performance, save, and user evidence |

Machine-readable ownership and scenario mapping are in [traceability](../../project-control/REQUIREMENTS_TRACEABILITY.json). Every implementation issue names its requirement IDs and scenario IDs. Adding a new mandatory requirement updates both records and the run history.

## Working defaults for implementation

Start with a Windows desktop proof and keyboard/mouse, while making layouts touch-aware and testing mobile packaging early. Use single-player offline simulation; no world advancement while the application is closed by default. Pause while the player composes commands. Support controlled fast-forward with explicit interruptions. Keep party, heir, and institutional continuation as proposed continuity mechanisms until G-8 user testing selects their presentation.

A bundled local model or complete offline installation path must support the baseline language experience. A no-model menu mode is recovery and accessibility support, not fulfillment of the natural-language product promise. Do not sell different simulation intelligence by model tier.

## Player control and fairness

The player chooses an active observer and controls only actors legitimately under their authority. The player can request cooperation from others. Delegated orders incur communication and understanding rules. A profession is not a hard prerequisite to try an action, although licensing, tools, knowledge, physical ability, and social authority can matter.

Expose known costs and estimated risks without revealing hidden outcome probabilities that the character could not know. A dangerous but valid action may be attempted; a parse failure must never consume supplies as if the player attempted it. Irreversible or materially ambiguous commands require a specific interpretation preview.

## Scope change procedure

A proposed reduction or expansion names the affected requirements, save/content impact, scenario impact, and release implications. The maintainer approves changes to product intent. Engineering may tune algorithms and performance budgets within those requirements, recording consequential choices. No era ceiling or world-size minimum is invented to make a milestone look complete.
