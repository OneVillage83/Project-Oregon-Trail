# Content packs, extensibility and modding architecture

Version 0.2 | Owner: content/tooling lead

## Pack structure

A pack has namespace, version, compatible rules/schema range, dependencies, source/license metadata, content hashes and capability requirements. It can contain prototypes, materials, processes, skills, conditions, technology definitions, scene layouts, biographies, localization, sounds and asset manifests. Pack identity and load order are part of the save manifest.

References use stable namespaced IDs. Never resolve a missing dependency by taking an unrelated similarly named object. Duplicate IDs, dependency conflicts and unsupported required capabilities fail compilation with precise diagnostics.

## Authoring and compilation

Source files are readable JSON/YAML or appropriate art/audio formats. Build-time compilation validates schemas, references, units, process accounting, prerequisite cycles, asset states, localization keys and compatibility. Produce a deterministic runtime pack with manifest/checksums. Runtime loading repeats safety-critical validation.

Authoring changes go through source review, fixtures and an auditable run-history entry. Large binary art and model weights use approved artifact storage/distribution rather than ordinary source history. Licensing is tracked per asset and checkpoint, not assumed from the engine license.

## Extensions

New entities/materials/processes should reuse existing affordances and rule modules. A genuinely new physical or social operation requires an explicit registered handler, typed parameters/events, persistence changes, observer-safe presentation and tests before data can request it. A pack cannot declare unsupported operations implemented by prose.

Keep cosmetic packs separate from rule-affecting packs. Changing an icon need not invalidate authoritative replay; changing material strength can. Manifests classify these effects and save compatibility checks enforce them.

## Mod trust levels

Official packs are reviewed and distributed through the approved authenticity path. Data-only mods use the same bounded compiler/runtime contracts and have no arbitrary script/native access. Developer extensions are separately enabled with explicit risk disclosure and are not the baseline consumer mod format. Do not advertise a secure arbitrary-code sandbox before it exists and is tested.

A modded save records exact versions and dependencies. Removing a required mod prompts an explicit migration/compatibility decision; no silent missing-entity deletion. Preserve a recovery copy before changing a campaign's content stack. User-authored scenarios can change rules intentionally but must be identified as a different rules/content profile.

## Authoring tools

Provide prototype/process inspectors, dependency graph views, scene/anchor editors, knowledge/evidence inspectors, technology viewers, scenario runners and balance reports. Tools should operate on the same validation and simulation APIs as the game. An editor preview cannot invent state that runtime cannot reproduce.

## Acceptance

SC-CONTENT tests valid/invalid references, unknown capabilities, source/sink accounting, dependency cycles, missing visual states, localization and mod removal. SC-SECURITY tests untrusted package limits. SC-REPLAY verifies that a rule-affecting content change is detected rather than silently producing a different campaign.
