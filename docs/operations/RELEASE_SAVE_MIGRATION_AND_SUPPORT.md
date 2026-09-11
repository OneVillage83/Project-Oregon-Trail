# Release, migration and support runbook

Version 0.2 | Owner: release/QA lead

## Release manifest

Record source commit, clean build environment, engine/binding/compiler, dependency/runtime/model hashes, content versions, schema/rules/save versions, supported devices, test evidence, known defects and user-facing scope. Rebuild from pinned inputs. Where signing is required, use approved release infrastructure and record verification without exposing signing material.

## Pre-release gate

Run contracts, native/unit/integration/replay suites, supported migrations, offline install/first-launch/play/save/reload, low-storage/suspension and nominated-device performance. Verify provenance/notices/disclosures and review accessibility/tutorial/grounding. Required unrun tests remain blockers or explicit support exclusions.

Approve actual included systems/eras and describe them consistently. Future architecture is not shipped functionality. Record reviewers, residual risks and rollback decision.

## Updates

Separate code, rules/content, cosmetics and optional models. Declare compatibility impact. Stage downloads with adequate disk space, validate authenticity/checksums and promote only after validation. Failed installation retains the last usable package and save.

Model replacements repeat qualification but do not reparse saved intents. Rule changes may affect future simulation and need version policy. Missing dependencies cannot be silently replaced in an old campaign.

## Save migration

Verify source version, copy the original, migrate the copy transactionally, validate accounting/queries, record evidence and promote the copy. Keep recovery data until retention policy permits cleanup after verified play. Interrupted migrations preserve recoverability. Explain downgrade limitations before updating.

## Incident response

For corruption, unauthorized mutation or serious information leakage, stop the affected rollout where possible, preserve failing fixtures/version evidence, assess affected versions, provide a tested safe build/repair, communicate impact/recovery boundaries and add regression tests. Never promise recovery of lost progress without evidence.

## Support intake

Collect build/platform, minimal reproduction and expected/observed outcome. Offer a redacted offline diagnostic export with preview; raw prompts and full saves are voluntary. Mark potential spoilers/private content. Do not require external account connectivity to continue baseline play.

Prioritize corruption/authority/knowledge failures over cosmetic defects. Repair the owning world/projection logic rather than masking defects through narration. Update run history with fixes and actual checks.

## Completion

Exercise installation, offline operation, update failure, migration, restoration and rollback on supported configurations. This runbook is a specification; writing it does not perform those exercises.
