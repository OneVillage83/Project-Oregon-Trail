# Accessibility, localization and onboarding

Version 0.2 | Owner: UX/content lead

## Information equivalence

Every input/presentation path should expose the same legitimate knowledge. Accessible descriptions cannot reveal an undetected clue, exact hidden measurement or secret door. A keyboard user must not need to guess a mouse-only entity reference. Perception-dependent cues have text/non-color alternatives after detection.

## Interaction requirements

Support keyboard focus order, remappable controls, pointer/touch targets appropriate to display size, scalable text, readable contrast, reduced motion, subtitles and distinct audio volumes. Avoid color as the only indicator of danger, ownership, evidence or task state. Provide persistent observer/time indicators and clear cancel/confirm actions.

Test small screens with virtual keyboards, large text and pinned panels. Preview overflow must scroll without hiding critical limits or confirmation. Tooltips and journals should remain accessible without hover. Speech input is optional, editable and does not replace keyboard/touch.

## Language independence

Canonical commands use stable IDs, enum values and explicit units, not localized display strings. Localized text uses keys, parameterized messages, pluralization and context. Do not assemble grammatically fragile sentences by concatenating translated fragments. Names and in-world documents preserve source language/provenance where relevant.

Formatting conversions are presentation-only; decimal separators, units and currencies cannot change authoritative quantities. Parsing localized natural language requires a separately evaluated corpus. Supporting a model's language does not prove the game's localization is complete. Each shipping locale qualifies commands, UI, content, tutorial and fallback templates.

## Tutorial design

Teach through the actual core loop: select an object; express a goal; inspect the interpretation; commit a bounded action; observe consequences; understand uncertainty and time; cancel or change a plan. The crossing introduces alternative solutions without forcing one exact phrase. The investigation teaches that an observation differs from a conclusion. A project teaches supplies, labor and prerequisites.

Provide contextual help describing currently supported capabilities. Unsupported requests should explain the boundary and suggest only genuinely supported alternatives. Do not promise unlimited real-world actions. Explain parse failure, validation failure, simulation failure and infrastructure failure differently.

## Cognitive load and pacing

Start with concise results and expandable details. Allow management-heavy and scene-focused layouts. Group routine notifications while preserving significant commitments, deaths, losses and decisions. Let players review accepted plans and spending/risk limits before fast-forward. A time-advance summary must reference actual events rather than fabricated prose.

## Playtest protocol

Recruit unfamiliar testers using different input/accessibility needs. Observe task completion, misunderstood commands, excessive clarification, inaccessible information, unreadable layouts and loss of control during time advancement. An initial target is 10 of 12 unfamiliar testers completing opening tasks without developer intervention; record sample limits and do not generalize it into universal accessibility certification.

SC-ACCESS covers keyboard/touch/description equivalence and no leaks. SC-UI covers layout/cancel/preview. SC-ONBOARDING covers opening tasks, uncertainty and alternative approaches. No legal accessibility-compliance claim is made by this specification alone; shipping requirements receive platform/legal review.
