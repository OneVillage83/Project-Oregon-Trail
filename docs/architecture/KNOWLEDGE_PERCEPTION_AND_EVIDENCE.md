# Knowledge, Perception Mode and evidence architecture

Version 0.2 | Owner: gameplay/knowledge lead

## Four different layers

World truth is authoritative state. Observable state is what a particular sensor/position could expose. An observation is what an actor detects under current skills, attention and conditions. Knowledge/belief is what the actor retains, learns, suspects or has been told. Player presentation consumes that last permitted projection; it does not directly inspect hidden components.

## Records

A fact/proposition has typed subject, predicate, value or relation, temporal scope and provenance. An observation records observer, acquisition event/time, source, sensory modality, precision/uncertainty and retention rules. A belief references supporting and contradicting claims with source identity and confidence; confidence is not truth. A hypothesis is stored separately until tested. A report can contain a false proposition without changing the world fact it describes.

Use exact provenance IDs, not only generated summaries or embeddings. Retrieval can use indexed tags/text and optional embeddings, but access filtering happens before model retrieval and after results are assembled. Approximate similarity must never override disclosure permissions.

## Perception resolution

Combine general perception with domain skill, familiarity, attention, distance, lighting, fatigue/injury, weather, concealment and clue salience. The formula in the foundation is conceptual; balance constants are versioned data calibrated by tests. A hunter reads tracks, a carpenter reads construction, and a physician reads bodily signs. These observations can overlap without collapsing all expertise into one universal stat.

Passive viewing reveals obvious facts. Deliberate examination/search spends real time or resources. Persist observation attempt identity and conditions. Reopening Perception Mode under unchanged conditions reuses the result, not a fresh free roll. A different observer, improved light, a tool, additional time or new evidence can justify another attempt. Repetition alone is not unlimited skill training.

## Visible versus inferred information

A bookshelf can be visible while its mechanism remains unknown. An accessible label may say bookshelf, not secret-passage switch. Selected object tokens do not encode hidden roles. A clue that the character has observed can appear in the journal after leaving, with its observation time and potentially stale precision.

A player's proposed inference is allowed, but the simulation does not certify it simply because it is plausible. Comparing measured interior/exterior dimensions can reveal a discrepancy within measurement error; it does not establish the purpose or contents of a hidden space.

## Evidence provenance

Before an event depends on geometry, witnesses or tools, commit those facts. The event creates traces through material and behavioral rules. Evidence records creation event, original and current location, condition/decay, collection history, access history and observed interpretations. Moving or disturbing evidence changes it and may affect later confidence. The model never invents the culprit or new evidence to make an accusation work.

Preserve secret case truth in developer-only storage/projections. Player case files contain observations, claims, contradictions and institutional findings. A verdict is an institutional action, not a mutation of historical truth. False accusations and unsolved cases remain possible.

## Communication and memory

Information becomes available after a valid channel delivery and actor acquisition rule. A party member scouting alone knows findings before the party does. News, letters, newspapers, radio and later channels share a delivery abstraction with era-dependent latency, reach, cost and reliability. Beliefs can remain stale after the world changes.

Memories may be summarized for language, but summary text cannot create authoritative facts. Permanent significant records retain provenance. Any forgetting/degradation rule must be explicit and distinguish loss of actor recall from deletion of world history.

## Projection security

UI labels, tooltips, map legends, autocomplete, action suggestions, narration, dialogue, search, audio cues and accessibility descriptions all use the same observer policy. Caches include observer and knowledge revisions. A view of one NPC cannot reuse another NPC's secret facts. Debug inspection requires an explicit developer mode and never changes normal gameplay truth.

Differential tests compare serialized projection payloads for observers with/without a secret. Verify no hidden IDs, predicate names, counts, exact quantities or error reasons leak. Timing side channels are assessed where they reveal gameplay-critical information; response coarsening is preferable to pretending this is adversarial multiplayer security.

## Acceptance

SC-PERCEPTION tests skill differences and reroll resistance. SC-KNOWLEDGE tests rumors, stale facts, dialogue, cache and accessibility parity. SC-CASE verifies event-to-trace provenance, contamination, contradictory claims and unsupported accusation handling. These scenarios are required before generated dialogue is allowed to carry important clues.
