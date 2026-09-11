# Ecology, weather, terrain and resources

Version 0.2 | Owner: world-systems lead | Requirement PR-014

## Owned state

Own regional climate parameters, current weather fields, hydrology state, terrain travel modifiers, vegetation/resource stocks, wildlife cohorts and environmental hazards. Spatial generation supplies topology and baseline suitability; ecology changes mutable conditions. Distinguish actual conditions from forecasts and actor observations.

## Update model

Use deterministic, bounded, multi-rate updates: short-lived weather near consequential activities; scheduled daily/seasonal changes regionally; aggregated stock/cohort dynamics at distance. Exact timesteps and parameter ranges are content/rules versions. Split integration around floods, fires, harvests and other consequential events. Reloading a region cannot reroll its history.

Weather is not selected by a narrator to make a story interesting. Forecasts derive from an explicit knowledge/tool model and may be uncertain. A character's 'return if weather worsens' condition uses observable/assessed weather, not the future schedule.

## Resources and wildlife

Every harvest has source stock, removal, yield, waste, labor/tool requirements and possible renewal. Diminishing resources affect future availability and local economies. Wildlife can use aggregate cohorts until a named/interaction-relevant animal is instantiated with corresponding cohort accounting. An animal used as transport/property remains individually persistent.

Regeneration, births, deaths and migration are explicit sources/sinks with bounded calibrated rules. Keep carrying-capacity and time-resolution assumptions visible in balance data. Do not infer ecological realism solely from a visually plausible map.

## Environmental effects

Rain, snow, heat, terrain and water conditions affect visibility, travel, fatigue, structural condition, food storage and exposure through typed domain effects. Route damage changes passability/capacity, not just scenery. Fires consume defined fuel/resources and create damage/smoke states under a bounded abstraction; do not implement real-world hazardous recipes or unrestricted physical chemistry.

Cross-region flows have one owner and a shared boundary ledger. Water/resource transfers must not be counted twice. Seasonal processes use the campaign calendar rather than the host computer's date.

## Observation and persistence

Maps can be stale. A road known to exist may have washed out; discovery updates the actor's knowledge. Hidden contamination, wildlife location or forecast confidence is filtered by the knowledge layer. Persist significant disturbances, stocks, cohort state, environmental event schedules and generator/rules versions.

## Acceptance

SC-ENVIRONMENT tests weather-triggered visibility/travel changes, depletion/renewal, route disruption, named-animal persistence and reload stability. SC-FIDELITY tests aggregation and stock conservation. SC-REGIONAL connects a weather disruption to a delayed shipment, inventory shortage, price response and a resulting opportunity without bespoke quest scripting.
