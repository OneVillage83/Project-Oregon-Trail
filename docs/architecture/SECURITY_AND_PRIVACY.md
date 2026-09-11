# Security, privacy and trust boundaries

Version 0.2 | Owner: security/build lead

## Assets and threat model

Protect save integrity, player privacy, system resources, model/content provenance and observer-secret information. Treat imported saves, mods, model packages, in-world documents and arbitrary input text as untrusted. This is initially an offline single-player game, not an adversarial multiplayer service; anti-cheat infrastructure is not a prerequisite.

World-secret isolation is a correctness boundary enforced by projections and tests. A technically sophisticated owner can inspect their local files; do not promise cryptographic secrecy of a fully local world from that owner. Do prevent accidental spoilers and unauthorized access through normal gameplay interfaces.

## Authority boundaries

Client inputs are requests, not state mutations. Bind initiating identity and allowed actors to the local session, not the model's claims. Validate every target, operation, parameter and resource limit. Generated text has no host tools or filesystem/database handles. In-world instruction-like text is data. No prompt can grant additional authority.

Keep the renderer and language context on observer-safe projections. Privileged developer inspectors are explicit and labeled; do not include their unrestricted views in normal player panels or exports by default. Caches and search results are scoped by observer/revision.

## Input and package validation

Bound JSON bytes, depth, lists, string lengths, planning expansions and recurring work. Reject duplicate JSON keys and nonfinite numbers. Validate archive extraction against path traversal, absolute paths, duplicate paths and excessive decompressed size. Verify schema versions and content hashes before loading. A checksum detects corruption; it does not authenticate an unknown publisher by itself.

Official distribution uses a reviewed authenticity/signing path and pinned manifests where the platform supports it. Third-party packs require explicit trust decisions. Data-only mods cannot run native code or arbitrary scripts. Developer-native extensions are a separate unsupported-by-default trust tier with clear warnings and a separate execution policy.

## Native/runtime safety

Use ownership-safe interfaces, checked quantities, bounded buffers, sanitizers and fuzzing. Restrict runtime network listeners; prefer in-process or local IPC adapters rather than exposing inference to a public interface. A desktop worker process may improve crash isolation, but an operating-system sandbox is a separate implementation/qualification task, not guaranteed by calling it a worker.

Model installation verifies known formats, sizes and hashes and handles failures without executing downloaded scripts. Avoid loading unneeded model capabilities. A failed backend falls back visibly; no secret cloud request.

## Privacy

Offline play is the default. Telemetry and crash uploads require explicit opt-in and a readable preview/policy. Keep player-entered text, personal names, local paths and raw prompts out of routine logs. Redact exports and never include platform credentials, access tokens or signing material. Diagnostics can contain spoilers; mark and scope privileged bundles.

Provide configurable local log retention and deletion. Save files remain player-controlled. Cloud sync, if later added, is opt-in and outside baseline correctness; conflicts preserve both versions rather than overwriting a campaign silently.

## Release review and incidents

Maintain dependency/model/content provenance and a vulnerability response process. For a corrupting update, stop rollout, preserve evidence, restore the last safe build and offer a tested migration/recovery path. Never ask players to upload an entire private save when a redacted trace is sufficient.

SC-SECURITY tests imported-data limits, path handling, invalid identities, prompt-like game data and unavailable model tools. SC-KNOWLEDGE tests normal-play information boundaries. SC-SAVE tests malicious/corrupt packages and recovery. A written policy is not evidence of completed security testing.
