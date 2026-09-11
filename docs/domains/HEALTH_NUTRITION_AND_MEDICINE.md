# Health, nutrition, injury, disease and care

Version 0.2 | Owner: health-systems/content lead | Requirement PR-013

## Scope and representation

Model health as consequential gameplay with explicit abstractions, not as real medical advice or a clinical simulator. Disease/therapy parameters and historical portrayals require research/editorial review before shipping. Do not generate real dosing or treatment instructions from a language model.

Health owns exposure history, latent condition states, symptoms, injuries, functional impairments, recovery trajectories and received care. Nutrition/needs own consumed food/water, coarse sufficiency, fatigue and rest accounting. Knowledge owns what patients/caregivers believe or observe. A hidden condition and a character's diagnosis are distinct records.

## State and progression

A condition instance references its content definition, onset/exposure event, stage, severity, modifiers, next scheduled transition and resolution. Injuries reference location/type/function and causal event. Use bounded calibrated state machines or hazard models, not arbitrary per-frame rolls. Random transition streams are reproducible and condition-scoped.

Nutrition consumes actual inventory and water sources; spoilage/contamination links to ecology and containers. Rest and care consume actual time, labor and facilities. Missing data or unmodeled clinical phenomena are explicit limitations, not invented symptoms.

## Observation and care pathway

Exposure → latent condition → detectable signs → examination → working diagnosis → proposed care → authorized treatment/monitoring → subsequent outcome. Not every stage is immediately observable. A physician uses acquired knowledge, era-appropriate tools, patient reports and observations. A diagnosis can be uncertain or wrong; the kernel does not reveal a hidden pathogen simply because the player asks a fluent model.

Care operations validate access, skill, equipment, supplies, time and patient/party authority. They schedule process effects rather than instantly setting health to perfect. Monitoring needs a recurrence/end condition and caregiver availability. Treatment interruption, side effects and limits follow reviewed game rules.

## Cross-system contracts

Consume FoodConsumed, WaterConsumed, ExposureOccurred, InjuryOccurred, Work/RestProgressed and CareApplied. Emit SymptomsChanged, FunctionChanged, CareRequired, Recovered and LifecycleRisk/Death events. Character capabilities update through committed effects, not independent UI deductions.

Contamination/care evidence can matter in investigations. Medicine changes through education, institutions, supplies and technology adoption. Quarantine is an institutional policy with real social/economic effects, not a global switch that stops all disease automatically.

## Player presentation and content boundaries

Present known symptoms, fatigue, care status and uncertainty. Separate gameplay abstractions from real-world claims. Do not portray a historically used treatment as effective without reviewed simulation rationale. Accessibility settings can reduce distressing presentation without changing saved causality unexpectedly; significant rule changes require a campaign mode/version policy.

## Balancing and persistence

Calibrate burdens so health creates decisions rather than constant opaque failure. Preserve condition IDs, exposure/care provenance, stage timers, modifiers and relevant observations across saves. Reopening a save cannot reroll onset or cure. Distant population health can aggregate, but named patients and commitments remain tracked.

## Acceptance

SC-HEALTH tests contaminated source versus actor knowledge, symptom delay, resource-limited care, monitoring schedule conflicts, interrupted treatment, recovery/death consequences and save/reload. Cross-domain tests link route delays to missing supplies and health effects. The model cannot diagnose from hidden truth or change condition state through prose.
