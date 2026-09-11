# World Action Language V1

## Status

Foundational architecture draft.

Internal shorthand should use **WALang** rather than `WAL` because `WAL` commonly means write-ahead log in software systems.

## Purpose

World Action Language (WALang) is the intermediate representation between free-form player intent and authoritative simulation execution.

Its core rule is:

> **WALang describes what an actor intends to attempt. It never declares what actually happens.**

Example:

Player:

> "Pull the blue book."

Valid intent:

```yaml
action: MANIPULATE
actor: player_character
target: blue_book
operation: PULL
```

Invalid outcome declaration:

```yaml
secret_passage_opens: true
```

Only the simulation may determine whether the book moves, whether it is a lever, whether a mechanism works, and what resulting events occur.

## Runtime pipeline

```text
PLAYER INPUT
    |
    v
LOCAL LANGUAGE MODEL / PARSER
    |
    v
WALang INTENT
    |
    v
REFERENCE RESOLVER
    |
    v
ACTION VALIDATOR
    |
    v
PLANNER / SCHEDULER
    |
    v
AUTHORITATIVE SIMULATION
    |
    v
WORLD EVENTS + STATE CHANGES
    |
    +--> KNOWLEDGE / MEMORY
    +--> VISUAL RENDERER
    +--> NARRATIVE / DIALOGUE REALIZATION
    |
    v
PLAYER PRESENTATION
```

## Design requirements

WALang V1 must support:

1. AI never declaring outcomes.
2. Authoritative deterministic/rule-driven simulation.
3. Separate storage for intent, execution plan, and world events.
4. Known, observed, suspected, and hypothetical information.
5. Sequential, parallel, conditional, fallback, and recurring plans.
6. Goals without specified methods.
7. Methods without guaranteed outcomes.
8. Composable object affordances.
9. Reference resolution against actor-accessible knowledge.
10. Future NPC use of the same language.
11. Mouse/touch/visual references inside natural-language commands.
12. Survival across technological eras.
13. Delegation, policies, and organization-scale directives.
14. Full inspectability/debuggability.
15. Replaceable natural-language parsing models.

## Command hierarchy

At the highest level:

```text
COMMAND
├── ACTION
├── PLAN
├── GOAL
├── DIRECTIVE
├── QUERY
└── HYPOTHESIS
```

### ACTION
A concrete intended operation by one or more actors.

### PLAN
Multiple actions with sequencing, parallelism, conditions, or fallbacks.

### GOAL
A desired state without necessarily specifying the method.

### DIRECTIVE
A persistent policy or delegated objective operating over time.

### QUERY
A request to retrieve, compare, calculate, remember, or ask about known information.

### HYPOTHESIS
A proposition the actor wants to test without asserting it as fact.

## Action structure

A general action should support these semantic fields where relevant:

```text
WHO?
DOES WHAT?
TO WHAT?
HOW?
UNDER WHAT CONDITIONS?
FOR HOW LONG / HOW FAR?
TOWARD WHAT PURPOSE?
```

Canonical conceptual form:

```yaml
intent_id: INT-284193

actor:
  ref: Jacob

action:
  type: SCOUT

target:
  kind: terrain
  selector:
    relation: upstream
    from: current_camp

parameters:
  max_distance: 5_miles
  transport: horse

constraints:
  - type: ABORT_IF
    condition:
      weather_severity: worsening

purpose:
  find: safer_crossing

priority: normal

schedule:
  start: now
```

## Declarative rather than micro-commanded

WALang should encode meaningful intentions rather than generate hundreds of animation-level operations.

Player:

> "Build a raft."

Desired representation:

```yaml
action: BUILD
target:
  prototype: raft
goal:
  capable_of:
    - carrying_party
    - crossing_current_river
```

The simulation determines:

- materials;
- labor;
- tools;
- process;
- skill requirements;
- duration;
- errors;
- interruptions;
- success or failure.

## Action families

Action vocabulary should be broad and composable rather than a huge list of bespoke commands.

### Perception and investigation

- OBSERVE
- PERCEIVE
- EXAMINE
- SEARCH
- TRACK
- COMPARE
- MEASURE
- TEST
- LISTEN
- SMELL
- RECALL
- INFER

### Movement

- MOVE
- TRAVEL
- SCOUT
- FOLLOW
- FLEE
- APPROACH
- ENTER
- EXIT
- WAIT

### Object interaction

- TAKE
- DROP
- MANIPULATE
- OPEN
- CLOSE
- PULL
- PUSH
- TURN
- BREAK
- CUT
- DIG
- BURN
- POUR
- ATTACH
- DETACH
- USE

### Creation and transformation

- CRAFT
- BUILD
- REPAIR
- MODIFY
- DISASSEMBLE
- SALVAGE
- COOK
- PROCESS

### People and organization

- ASSIGN
- HELP
- TEACH
- LEARN
- LEAD
- GUARD
- ESCORT
- CARE_FOR
- REST
- DELEGATE

### Social

- ASK
- TELL
- OFFER
- REQUEST
- NEGOTIATE
- THREATEN
- PERSUADE
- DECEIVE
- ACCUSE
- INTERVIEW

### Economy

- BUY
- SELL
- TRADE
- BARTER
- HIRE
- FIRE
- LEND
- BORROW
- INVEST

### Medical

- EXAMINE_PATIENT
- DIAGNOSE
- TREAT
- ADMINISTER
- BANDAGE
- OPERATE
- QUARANTINE
- MONITOR

The exact production ontology may consolidate some verbs under operations, but the semantic coverage should remain.

## Compositional actions

Avoid hard-coded commands such as `PULL_BOOK` or `MOVE_BOOKSHELF`.

Prefer reusable structure:

```yaml
action: MANIPULATE
operation: PULL
target: blue_book
```

```yaml
action: MANIPULATE
operation: ROTATE
target: painting
direction: clockwise
```

```yaml
action: MANIPULATE
operation: PUSH
target: bookshelf
direction:
  relative_to: wall
  vector: away
```

## Object affordances

Objects expose likely operations, but affordances should not become a rigid exhaustive action whitelist.

Example book:

```text
TAKE
READ
OPEN
CLOSE
PULL
BURN
TEAR
GIVE
SELL
```

Example horse:

```text
RIDE
FEED
WATER
EXAMINE
LEAD
LOAD
TREAT
SELL
```

Novel uses should be evaluated through object properties where possible.

Example:

> "Use the rifle barrel as a lever."

```yaml
action: USE_AS_TOOL
object: rifle_barrel
functional_role: lever
target: wagon_axle
```

The simulation evaluates geometry, material strength, condition, required force, and consequences.

## Reference resolution

Players refer to entities naturally rather than through IDs.

Examples:

- "the blue book";
- "Sarah";
- "that tree near the river";
- "the horse Jacob rode yesterday";
- "the second wagon";
- "the man who sold us the rifle".

WALang should support selectors such as:

```yaml
target:
  selector:
    type: book
    color: blue
    location:
      container: west_bookshelf
```

References resolve against information the actor/player can legitimately access, not unrestricted omniscient world state.

## Conversational references

Pronouns and previous topics require discourse state.

Example:

Player: "Ask Thomas about the bridge."

Then:

> "Tell him to inspect it tomorrow."

`him` resolves to Thomas and `it` resolves to the bridge when confidence is high enough.

## Visual references

Touch/mouse selection should provide precise entity references.

Example flow:

1. Player taps bookshelf.
2. UI stores `selected_entity = bookshelf_1842`.
3. Player says "Check behind this."
4. Parser resolves `this` to `bookshelf_1842`.

This combines conventional interaction with language and reduces ambiguity.

## Epistemic state

WALang must represent uncertainty explicitly.

Possible states:

```text
known
observed
suspected
hypothetical
reported
remembered
```

Confidence may be attached when appropriate.

Example:

```yaml
epistemic_status: observed
confidence: 0.63
```

## Hypothesis testing

Player:

> "I think there may be another room behind that wall. Measure the inside and compare it to the outside dimensions."

Representation:

```yaml
plan:
  type: INVESTIGATION

hypothesis:
  proposition:
    hidden_space:
      behind: west_wall

steps:
  - action: MEASURE
    target: building_exterior
    dimensions: true

  - action: MEASURE
    target: current_room
    dimensions: true

  - action: COMPARE
    inputs:
      - result: building_exterior_dimensions
      - result: interior_dimensions

goal:
  evaluate:
    hypothesis: hidden_space_behind_west_wall
```

The language does not assert the hidden space exists.

## Perception actions

Perception Mode may generate:

```yaml
action: PERCEIVE
actor: active_character
scope:
  location: current_scene
attention:
  level: normal
```

A deliberate search is different:

```yaml
action: SEARCH
scope:
  location: current_room
attention:
  level: thorough
time_budget:
  duration: 20_minutes
```

The simulation uses perception, relevant skills, lighting, fatigue, clue salience, concealment, time, and other factors to determine detected observations.

## Multi-action commands

Player:

> "Stay here today. Have Thomas and William gather timber while Margaret examines Sarah, and send Jacob upstream on horseback."

```yaml
plan_id: PLAN-1842
execution: PARALLEL

actions:
  - actor: party
    action: HOLD_POSITION
    duration: 1_day

  - actor: [Thomas, William]
    action: GATHER
    target:
      resource: suitable_timber

  - actor: Margaret
    action: EXAMINE_PATIENT
    target: Sarah

  - actor: Jacob
    action: SCOUT
    target:
      relation: upstream
    transport: horse
```

## Sequential plans

Player:

> "Cut down two trees, bring the logs back, then start building the raft."

```yaml
plan:
  execution: SEQUENTIAL

steps:
  - id: fell_trees
    action: HARVEST
    resource: tree
    quantity: 2

  - id: transport_logs
    action: TRANSPORT
    items:
      from_result: fell_trees
    destination: camp

  - id: build_raft
    action: BUILD
    target: raft
    materials:
      include_result: transport_logs
```

## Conditions and interruption rules

Player:

> "Follow the tracks unless they lead into open terrain."

```yaml
action: FOLLOW
target:
  type: tracks

constraints:
  - type: ABORT_IF
    condition:
      terrain:
        exposure: open

on_abort:
  action: RETURN
  destination: current_camp
```

Player:

> "If anything looks dangerous, come back."

```yaml
interrupt_rules:
  - condition:
      actor_assessment:
        danger: significant
    response:
      action: RETURN
```

Because this uses actor assessment, personality and risk tolerance may affect the result.

## Fallbacks

Player:

> "Try repairing the axle with iron first; if there isn't enough, use hardwood."

```yaml
plan:
  type: FALLBACK

options:
  - action: REPAIR
    method:
      material: iron

  - action: REPAIR
    method:
      material: hardwood
```

## Goals versus methods

Player:

> "Get us across the river safely."

```yaml
goal:
  type: REACH
  destination: opposite_bank
constraints:
  risk_tolerance: low
```

Player:

> "Build a raft to get us across the river."

specifies a method as well as a goal.

WALang must support both abstraction levels.

## Delegation

Player:

> "Thomas, figure out the safest way to repair the wagon."

```yaml
action: DELEGATE
actor: Thomas

goal:
  restore:
    target: wagon
    property: operational

optimization:
  primary: safety

authority:
  resources: reasonable
```

Thomas plans using Thomas's own knowledge, ability, personality, and authority.

## Authority and social requests

The player cannot directly control actors who are not under their authority.

> "Tell Elias to give us all his money."

must be encoded as a social request, not an inventory transfer.

```yaml
action: REQUEST
target: Elias
content:
  action_requested:
    type: TRANSFER
    asset: all_money
```

Elias decides how to respond.

## Dialogue semantics

Player:

> "Ask Margaret whether Sarah's illness could be from the river water."

```yaml
action: ASK
target: Margaret
topic:
  proposition:
    cause:
      condition: Sarah.illness
      possible_source: river_water
```

Margaret's response must be derived from her beliefs and knowledge.

## Lies and deception

Player:

> "Tell the sheriff we were never in Blackridge."

If the player knows the statement is false:

```yaml
action: TELL
target: sheriff
statement:
  proposition:
    player_present_in_Blackridge: false
speaker_epistemics:
  knows_statement_false: true
```

The simulation handles credibility, evidence, contradictions, memory, and later consequences.

## Negotiation

Player:

> "Offer the three hides for the rifle and forty rounds."

```yaml
action: OFFER
target: merchant

give:
  items:
    selector: buffalo_hide
    quantity: 3

request:
  - item: rifle
    quantity: 1
  - item: cartridge
    quantity: 40
```

Player:

> "Start at forty dollars, but go no higher than fifty."

should add negotiation constraints rather than simulate a completed transaction.

## Qualitative constraints

Human instructions frequently use relative terms.

Examples:

- "Don't take too many risks." -> low risk tolerance.
- "Go as quickly as you safely can." -> optimize travel time subject to acceptable risk.
- "Spend whatever is reasonable." -> contextual budget policy.

The simulation may interpret these through personality, circumstances, prices, authority, and prior preferences.

## Time and scheduling

Time is first-class.

Possible schedules include:

```yaml
schedule:
  start: now
```

```yaml
schedule:
  start:
    event: sunrise
```

```yaml
schedule:
  start:
    after: Sarah_recovers
```

```yaml
duration:
  until:
    condition:
      rain: stops
```

## Recurring actions

Player:

> "Have Margaret check Sarah every two hours tonight."

```yaml
action: MONITOR
actor: Margaret
target: Sarah

schedule:
  recurrence:
    every: 2_hours
  until:
    event: sunrise
```

## Communication quality and misunderstanding

WALang represents intended meaning. A separate communication system may model whether the instruction is heard, translated, remembered, or understood correctly.

This becomes particularly useful for:

- language barriers;
- hearing limitations;
- messengers;
- written orders;
- telegraph/radio errors;
- later communication technologies.

## Validator behavior

The validator checks whether an intent can enter simulation execution.

Checks include:

- actor exists;
- target resolves;
- actor can reasonably reference target;
- action is semantically meaningful;
- authority is valid;
- scheduling is coherent;
- schema is valid;
- referenced resources/methods are understood.

The validator should not reject an action merely because success is unlikely.

Example:

> "Jump across the 25-foot ravine."

may be a valid action with an extremely poor outcome probability.

## Failure categories

### Parse failure
The parser cannot determine the intended structure.

### Validation failure
The intent is understood but cannot be resolved cleanly, such as two equally plausible blue books.

### Simulation failure
The action is valid and attempted but does not succeed.

These must remain distinct in logs and UI.

## Ambiguity

The system should clarify only when ambiguity is materially unresolved.

Player:

> "Give him the rifle."

If two equally plausible people are present, request clarification.

If the current conversation clearly concerns one merchant, resolve the reference automatically.

Confidence thresholds should prevent both reckless guessing and constant interruption.

## Optional interpreted-action preview

Before execution, especially for complex commands, the UI may show a compact interpretation:

```text
1. Remain at camp today.
2. Thomas + William gather raft timber.
3. Margaret examines Sarah.
4. Jacob scouts upstream by horse.
```

Players may be able to disable or minimize this preview once they trust the parser.

## Simulation output

The simulation returns structured events rather than prose.

Example:

```yaml
event_id: EVT-19324
type: SCOUT_COMPLETED
actor: Jacob
elapsed_time: 3h41m

results:
  distance: 4.8_miles

discoveries:
  - type: river_crossing
    location: REGION_NODE_4428
    depth_estimate: 0.93_m
    current: moderate

  - type: tracks
    category: wagon
    apparent_age: 1_to_3_days

state_changes:
  Jacob.fatigue: +17
  horse_2.fatigue: +19
```

The narrative renderer and visual renderer consume this same authoritative event/state data.

## Intent, execution, and events are separate

Store three layers:

### WALang intent
What the player requested.

### Execution plan
How the simulation decomposed and scheduled the request.

### World events
What actually occurred.

This separation enables debugging, replay, provenance, balancing, and persistent historical records.

## NPCs should eventually use WALang

Player and NPC actions should enter the same authoritative execution framework.

A merchant, physician, criminal, hunter, mayor, or worker differs by:

- goals;
- knowledge;
- personality;
- resources;
- skills;
- planning ability;
- authority.

They should not require entirely separate physics or world-rule systems.

## Technological extensibility

WALang should remain conceptually stable across centuries.

1843 may include:

- wagon travel;
- letters;
- hand tools.

Later eras may include:

- automobiles;
- telephones;
- electrical systems;
- aircraft;
- computers.

New technology should mostly add new entities, materials, processes, skills, knowledge, and affordances rather than require a new interaction language.

## Organization-scale directives

WALang must eventually scale from individual action to persistent policy.

Example:

> "We are staying in Clearwater for the winter. Find work for anyone who wants it, rent somewhere inexpensive for everyone, and keep at least three months of food in reserve."

This becomes a directive containing employment, housing, and reserve goals.

Later, an organizational player might issue:

> "Prioritize school construction in settlements with more than 1,000 residents."

The same intent architecture should support that scale.

## Key examples

### Investigation

> "Before touching anything, have Jacob examine the mud and footprints. Margaret can check the body. Compare the room dimensions to the exterior because I think there may be hidden space behind the bookshelf."

This is a parallel investigation plan containing evidence-preservation constraints and a hypothesis test.

### Improvised engineering

> "Empty four barrels, seal them, strap them underneath the wagon, unload everything except food and medicine, and have Thomas estimate whether it will float before anyone enters the water."

This is a sequential transformation/evaluation plan. The simulation determines buoyancy and structural safety.

### Social investigation

> "Don't accuse him yet. Ask where he was last night, casually mention the tracks by the window, and watch how he reacts."

This is a sequential social strategy plus observation task. The suspect's behavior and the observer's perception determine what is learned.

## Architectural conclusion

WALang should be built as an **extensible ontology of agents, objects, transformations, information, communication, goals, constraints, conditions, and time**, not as a fixed list of game buttons represented in text.

The next closely coupled design layer is the **World Object and Affordance System**, because WALang supplies the verbs of the simulation while the object ontology supplies the nouns, properties, capabilities, and transformation rules those verbs operate upon.
