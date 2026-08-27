# Local AI Architecture

## Objective

Project Oregon Trail should use AI to provide natural-language freedom without making the game dependent on recurring cloud inference costs or allowing generative models to become the authoritative game engine.

The target architecture is **offline-first and model-replaceable**.

## Core separation

> **The language model understands language. The simulation understands the world.**

The local model is an interface and presentation component. It is not the source of truth.

## Primary AI roles

### 1. Action interpretation

Convert free-form player input into World Action Language (WALang).

Example:

Player:

> "Have Jacob scout about five miles upstream on horseback, but turn around if the weather gets worse."

Interpreter output conceptually becomes:

```text
ACTOR = Jacob
ACTION = SCOUT
DIRECTION = upstream
MAX_DISTANCE = 5 miles
TRANSPORT = horse
ABORT_IF = weather worsens
```

The model does not determine what Jacob finds or whether he succeeds.

### 2. Narrative realization

Convert authoritative simulation events into readable natural language.

Simulation output may contain:

```text
Jacob traveled 4.8 miles.
Crossing discovered at region node 4428.
Estimated depth: 0.93 m.
Current: moderate.
Wagon tracks detected, apparent age 1-3 days.
Jacob fatigue +17.
Horse fatigue +19.
```

The narrative model may express those facts naturally, but must not add unsupported discoveries.

### 3. NPC dialogue realization

NPC dialogue should be generated only from that NPC's current:

- knowledge;
- beliefs;
- memories;
- personality;
- goals;
- social relationship;
- intended speech act;
- willingness to deceive.

The simulation should decide the semantic intent of a lie, refusal, counteroffer, confession, or warning where possible. The model realizes the wording.

## Suggested model strategy

The architecture should not commit permanently to one model family, but current small local models make the approach practical.

A likely tiered design is:

### Action model
A very small function-calling / structured-output model specialized for natural-language-to-WALang translation. This model can potentially be in the hundreds-of-millions to low-billions parameter range because its job is narrow.

### Narrative/dialogue model
A somewhat larger local model used for prose generation and richer conversation where hardware permits.

The two roles may initially share a model for simplicity, but they should remain separate interfaces architecturally.

## Training strategy

Do not train a foundation model from scratch initially.

Preferred path:

1. adopt a suitable local model;
2. build WALang and authoritative simulator schemas;
3. generate high-quality natural-language/action pairs;
4. fine-tune the interpreter on game-specific action semantics;
5. use larger teacher models during development to synthesize edge-case examples;
6. distill/quantize into a smaller production model if useful.

Training examples should include:

- typos;
- slang;
- incomplete commands;
- pronouns;
- contextual references;
- multiple actions in one sentence;
- conditions;
- fallbacks;
- goals without methods;
- methods without guaranteed outcomes;
- negotiation;
- hypothetical investigation;
- object manipulation;
- delegation;
- ambiguity.

## Context discipline

Do not feed the language model the complete world database.

Construct a small context package containing only what is relevant and permitted for the current task, such as:

- current location;
- selected entities;
- current conversation;
- active character knowledge;
- recent events;
- relevant object metadata;
- available action schema.

This improves speed, mobile feasibility, privacy, and hallucination resistance.

## NPC knowledge isolation

A character cannot reveal information that is not in that character's accessible knowledge state.

The world may know a river contains a pathogen. A physician may only know that several people became sick after drinking river water. The dialogue model receives the physician's knowledge, not the hidden pathogen record.

## Validation firewall

Every structured action emitted by a model must pass deterministic validation before execution.

Validation checks include:

- schema correctness;
- actor existence;
- target resolution;
- authority;
- semantic validity;
- available references;
- permitted state access;
- constraints and scheduling validity.

No model-generated structure directly mutates authoritative state.

## Structured generation

Where runtimes support it, constrained generation should enforce JSON/schema/grammar-compatible WALang output.

This should be considered an additional reliability layer, not a replacement for validation.

## Device tiers

The game should support a swappable local-inference layer.

Possible tiers:

### Mobile Lite
- small action interpreter;
- procedural/template narration where needed;
- full authoritative simulation.

### Mobile Full
- small action interpreter;
- richer quantized local narrative/dialogue model.

### High-end mobile/tablet
- higher-quality local narrative model;
- larger context budget where useful.

### PC
- stronger local model options;
- optional enhanced language pack;
- same core simulation rules.

The player should not be playing a mechanically different game merely because a different language model is installed.

## Offline requirement

The baseline production game must not require:

- OpenAI API usage;
- Gemini API usage;
- Anthropic API usage;
- permanent inference servers;
- per-token player credits;
- required internet connectivity.

Cloud models may be used during development, testing, data generation, or optionally by modders/developers, but not as a required gameplay dependency.

## Speech input

Voice can be added as another input layer:

`Speech -> local speech recognition -> text -> action interpreter -> WALang`

Dedicated speech recognition may be more efficient than using a multimodal general-purpose model solely for transcription.

## Model-replacement boundary

The game should define stable interfaces such as:

```text
parse_player_input(context, text) -> WALang
realize_event(context, world_events) -> prose
realize_dialogue(npc_context, speech_act) -> prose
```

Any compatible local model/runtime should be replaceable behind those interfaces.

## Non-negotiable rule

> **AI may interpret and express the game. It may never become the authoritative source of what happened.**
