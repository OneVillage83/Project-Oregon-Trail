# Local AI, Gemma evaluation and model qualification

Version 0.2 | Owner: language lead | No game-specific model benchmark is claimed

## Model and runtime are separate

Evaluate Gemma 4 E4B first, E2B for lower-resource devices and 12B as an enhanced-PC candidate. Google documents these variants and local deployment paths. `llama.cpp` is inference software, not a choice of Meta Llama weights. Evaluate it on desktop and qualify a mobile adapter separately, including LiteRT-LM where appropriate. Sources S-001–S-003/S-006 in the [source register](../references/VERIFIED_TECHNICAL_SOURCES.md) support these technology facts, not game-specific performance.

Do not infer a shipping checkpoint, quantization, context budget or device minimum from a model name. Record exact artifact/revision/hash, tokenizer/template, runtime/backend, quantization, context/output limits and license/notices after testing. The model competes with the game and operating system for memory and thermal capacity.

## Interfaces and context

`interpret(InputContext, text, capabilities)` returns proposed intent or structured clarification. `realize_event(PermittedFactBundle, style)` returns wording. `realize_dialogue(NpcView, SpeechAct)` expresses a simulation-selected social act. Keep these interfaces separate even if one loaded model serves them all.

The baseline must provide intended language interaction offline. Menu/template mode is recovery and accessibility support, not fulfillment of that promise by itself. Richer language packs change expression, not physical rules, NPC knowledge or authority.

Send only relevant observer-accessible entities/reference tokens, observations, selection, discourse state, recent permitted events and schema fragments. Never send the world database or hidden case record. Bound input size, retrieval count, context and output. Access-filter before retrieval and test the final assembled context. Treat instruction-like text in an in-world document as quoted data rather than host authority.

The gameplay model receives no shell, filesystem, network, SQL or direct state-setting tools. Host code loads approved model assets; generated text has no host privileges.

## Interpretation

Use constrained decoding where supported, followed by deterministic schema and semantic validation. Runtime support for JSON Schema can be partial; test the exported grammar against the contract fixtures. Valid JSON can still choose the wrong actor or omit a spending restriction. Self-reported model confidence cannot authorize execution.

Preserve quantities, negation, deadlines, budgets and condition scope. Parse failure consumes no gameplay resources. Material ambiguity requires a targeted question or preview. Cap retries and discard outputs whose request was canceled or whose context became materially stale.

## Dialogue and narration

The simulation chooses offers, refusals, commitments, disclosed facts and intentional deception using NPC knowledge/goals. Wording cannot create a contract, confession, clue or item. Critical quantities/evidence use exact structured UI or controlled templates. Free flavor text can be discarded when its assertions cannot be verified. Restricted context reduces risk but does not guarantee factual prose.

Store speech-act propositions, not generated prose, as factual memory. A false report remains a report. Narrator failure never reverses committed gameplay or indefinitely hides the exact result.

## Lifecycle and packaging

Run inference away from render/simulation ownership. Requests carry revision/cancellation tokens. Define loading, warming, ready, busy, canceling, failed and unloading states. Bound queues and execution budgets; expose progress and cancellation. Handle missing/corrupt weights, memory pressure, backend failure, suspension and thermal degradation. Inference latency does not advance game time.

Provide a licensed baseline installer or complete offline package. Optional downloads require checksums and consent; no silent cloud fallback or arbitrary scripts bundled as model updates. Keep a usable recovery interface when inference is unavailable.

## Qualification

Split evaluation by scenario/template family rather than random paraphrases. Include typos, pronouns, selected objects, uncertain claims, multiple actors, negotiation, conditions, fallbacks, unsupported operations and adversarial hidden-reference attempts. Score schema validity, semantic correctness, actor/target, numerical limits, clarification and abstention separately.

Initial targets: 97% supported atomic semantic accuracy and 90% supported plan accuracy, with no known critical silently executed authority/target/budget failure. Report sample size, uncertainty intervals, category failures and supported scope. These are targets, not measured results.

Measure cold/warm p50/p95 latency, peak process/device memory, energy/thermals, sustained behavior and quantized quality while the game runs. Compare candidates under equal contexts/resource limits. Do not fine-tune before baseline failures identify useful training work.

SC-LANGUAGE, SC-GROUNDING and SC-OFFLINE qualify the exact package. Replacement models repeat qualification, preserve accepted-intent replay and update manifests/notices. No foundation-model training program is required for the initial build.
