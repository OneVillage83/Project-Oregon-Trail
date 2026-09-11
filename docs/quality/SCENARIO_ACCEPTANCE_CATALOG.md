# Scenario acceptance catalog

Version 0.2 | All runtime scenarios below are planned, not executed by this package

Each row becomes an executable fixture plus an integration assertion and, where relevant, a human test. Contract JSON fixtures in examples/contracts are a small seed and do not implement these gameplay scenarios.

| Scenario ID | Fixture and action | Required assertions |
|---|---|---|
| SC-OBJECT | Nested containers, damaged supports and two improvised tool families | No cycles/negative stock; property-based use; explicit unsupported model; persistent damage |
| SC-INTENT | Ambiguous people, selected object, quantities, stale context, unknown verb | Correct resolution/clarification; no invented outcomes; hard constraints retained; distinct errors |
| SC-SCHEDULER | Two tasks share one axe; equal-time work, cancellation and retry | Exclusive reservation; stable ordering; no duplication; completed partial work retained |
| SC-CROSS | Same party/cargo crosses by ferry, scouting or construction | At least three causal approaches; actual costs/time; load/conditions matter; reload mid-plan |
| SC-PERCEPTION | Hunter, carpenter, physician and novice inspect one room | Distinct justified observations; no free toggle rerolls; meaningful changed conditions permit retry |
| SC-KNOWLEDGE | Hidden clue, false rumor, stale map and observer switch | No leaks in context/UI/cache/audio/accessibility; belief differs from truth; sources retained |
| SC-CASE | Precommitted crime with traces, witnesses and contamination | Culprit/history fixed before questions; chain of custody; false accusation does not rewrite truth |
| SC-WORLD | Same seed visited in different orders and reloaded | Committed topology/entities remain; dependent geometry predates event; bounded generation failures |
| SC-FIDELITY | Promote/demote regions with cohorts, named actors and cargo | Population/stock/ownership preserved; pinned identities remain; shipments counted once |
| SC-SAVE | Terminate around commit; fill disk; corrupt/truncate export; migrate | Last valid state recoverable; no false success; original save preserved; valid recovery disclosure |
| SC-REPLAY | Snapshot + accepted intents under pinned versions | Same hashes; model not called; first divergence identified; compaction boundary respected |
| SC-LANGUAGE | Held-out typos, references, plans, negations, budgets and deadlines | Schema and semantic metrics separate; correct clarification; no critical silent constraint loss |
| SC-GROUNDING | NPC offer, refusal, rumor, confession and narration | Wording cannot add commitments/items/clues; exact critical facts; unsupported prose discarded |
| SC-OFFLINE | Clean installed package without network; model missing/corrupt | Baseline language/play/save/reload offline; visible recovery; no silent cloud request |
| SC-UI | Selection + pronouns; stale preview; cancel during inference | Stable target tokens; canceled result cannot execute; menu/text equivalence; clear task state |
| SC-VISUAL | River direction, damaged wagon, secret door and mixed-era town | Scene agrees with observed geometry/state; no accidental secret asset cue; valid fallback |
| SC-ACCESS | Keyboard, touch, large text, descriptions and subtitles | Equivalent permitted information; complete focus path; no hover/color-only dependency |
| SC-PROGRESSION | Repeated trivial observation versus novel practice and teaching | Diminishing trivial gains; event-derived skill; emergent role without class-granted knowledge |
| SC-PARTY | Split party, borrowed horse, observer change and member death | No telepathy/teleportation; custody versus ownership; authority enforced; tasks reconciled |
| SC-NPC | Need-driven NPC with impossible goal and request from stranger | Shared operations; bounded planning/backoff; refusal possible; no free resources |
| SC-COMMUNICATION | Letter, traveler report and later communication channel | Knowledge only after acquisition; cost/delay/failure; retelling retains source ancestry |
| SC-HEALTH | Exposure, delayed symptoms, limited supplies and interrupted care | Hidden condition distinct from diagnosis; actual care resources; timers survive reload |
| SC-ENVIRONMENT | Storm, depleted resource, wildlife cohort and named horse | Real route/visibility effects; explicit renewal/source-sink; no reload reroll/duplication |
| SC-ECONOMY | Expiring quote, barter, wages, loan and insufficient funds | Integer/currency accounting; atomic exchange; no silent price increase; obligations preserved |
| SC-LOGISTICS | Full cargo shipment crosses region boundary then route fails | One cargo identity; no double sale; valid reroute/delay; correct custody and delivery |
| SC-CRAFT | Substitute materials, unavailable tool, paused build and salvage | Valid functional substitution; stage accounting; no refund of spent work; retained progress |
| SC-REGIONAL | Road damage delays supplies, changes stock/price and opportunity | Entire causal chain uses real events; no injected shortage/quest outcome |
| SC-LAW | Unwitnessed offense, later report, jurisdiction and wrong finding | Knowledge/authority matter; institutional finding differs from truth; sanctions accounted |
| SC-CONFLICT | Attack/defend/flee/surrender with injury and witnesses | Shared time/equipment rules; nonviolent actions meaningful; no omniscient witnesses |
| SC-INSTITUTION | Budgeted policy, revoked office and competing public projects | Spending/role limits; persistent obligations; no free public works; orderly handover |
| SC-EDUCATION | Teacher, learner, school record and missing expertise | Time/resources/knowledge prerequisites; learning not instant; institutional records survive |
| SC-TECH | Knowledge without factory/power; blocked supply; mixed adoption | Discovery distinct from capability/adoption; prerequisites real; later-era mechanics supported |
| SC-TOWN | Funded timber-to-brick upgrade and maintained/replaced bridge | Real material/labor stages; persistent site/title; visuals follow completion; history retained |
| SC-CONTINUITY | Death/retirement, contested property, heirs and decades of change | Valid successors; no lost obligations; same places/lineage; history survives compaction |
| SC-TIMEPLAY | Standing orders, fast-forward, danger and spending boundary | Meaningful interruptions before unauthorized action; exact summaries; player agency preserved |
| SC-SECURITY | Invalid identity, adversarial document and malformed package | No extra model authority; bounded decoding/planning; safe extraction; consented diagnostics |
| SC-CONTENT | Bad references, dependency cycles, missing assets and removed mod | Compiler rejects incompatible pack; no silent entity deletion; provenance/compatibility checks |
| SC-ONBOARDING | Unfamiliar players attempt the opening and alternate solution | Understand intent/time/uncertainty; no exact-phrase trap; completion and friction recorded |

## Evidence format

For each run record scenario/test version, source commit, seed or fixture hash, accepted commands, engine/rules/content/model/runtime versions, hardware/build configuration, expected invariants, observed result and failure artifacts. For human tests record task completion, intervention, comprehension and accessibility findings without unnecessary personal identifiers.

A gate references specific run IDs, not only this table. Runtime assertions are evaluated from authoritative state/events and permitted projections. Do not grade world correctness using generated prose. Finite passing runs are evidence within their coverage, not proof of unlimited simulation fidelity.
