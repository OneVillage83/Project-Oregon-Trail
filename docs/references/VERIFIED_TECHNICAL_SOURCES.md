# Verified technical source register

Reviewed for this production package on 2026-09-10 (America/Los_Angeles). Sources are primary provider/project documentation. They support technology facts, not project-specific benchmarks, legal clearance or completed implementation. Recheck changing dependencies/platform policies at qualification and release.

| ID | Source | Used for |
|---|---|---|
| S-001 | [Google Gemma 4 overview](https://ai.google.dev/gemma/docs/core) | Current family, local formats and model-memory caveats; lead candidate selection remains a project proposal |
| S-002 | [Google Gemma Apache 2.0 terms](https://ai.google.dev/gemma/apache_2) | Provider license text; exact shipped artifacts/notices still reviewed |
| S-003 | [llama.cpp grammar documentation](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md) | Constrained output and JSON Schema support limitations |
| S-004 | [SQLite atomic commit](https://sqlite.org/atomiccommit.html) | Transaction durability mechanisms and assumptions |
| S-005 | [SQLite backup API](https://sqlite.org/backup.html) | Consistent backup path rather than blind live-file copying |
| S-006 | [Google LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) | A separately evaluated local/edge inference runtime candidate |
| S-007 | [Godot GDExtension C++ workflow](https://docs.godotengine.org/en/stable/tutorials/scripting/cpp/gdextension_cpp_example.html) | Native binding workflow and platform/compatibility requirements |
| S-008 | [Steamworks Content Survey](https://partner.steamgames.com/doc/gettingstarted/contentsurvey) | AI content/disclosure and live-generation review requirements |
| S-009 | [python-jsonschema validation](https://python-jsonschema.readthedocs.io/en/stable/validate/) | Draft 2020-12 validation and schema checking for development contracts |
| S-010 | [jsonschema 4.26.0 package](https://pypi.org/project/jsonschema/4.26.0/) | Pinned architecture-validation dependency, not a shipped game dependency |
| S-011 | [llama.cpp project](https://github.com/ggml-org/llama.cpp) | Runtime/model distinction and native inference project |

## Repository sources

The preserved foundation at commit dbff86a9d512488533ffc2d47319a5bfa49d8ebe provides PROJECT_VISION, CORE_DESIGN_PRINCIPLES, PERCEPTION_AND_RENDERING, WORLD_SIMULATION_AND_GENERATION, LOCAL_AI_ARCHITECTURE and WORLD_ACTION_LANGUAGE_V1. The existing change policy and RUN_HISTORY govern audit logging. Production specs link these principles to implementation work; no complete missing conversation transcript is claimed recovered.

## Source discipline

External release facts and licenses are dated, replaceable evidence. In-game scientific/historical/medical content requires its own research and editorial provenance when authored. Fictional fixture names and balance rules are design choices, not external historical facts.
