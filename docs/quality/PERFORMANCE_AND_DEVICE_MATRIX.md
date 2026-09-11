# Performance budgets and device qualification

Version 0.2 | Targets, not measured results | Owner: performance/QA lead

## Measurement policy

Every number names a workload, hardware, OS, build, rules/content, model/runtime/quantization, cold/warm state and duration. Report percentiles and peak memory, not only average tokens per second. Test the model while the game runs. No minimum device is currently qualified.

## Initial target envelope

| Area | Planning target | Qualification requirement |
|---|---|---|
| Desktop presentation | 60 FPS target under baseline slice | Frame-time p95/p99 and sustained traces; not inferred from empty scene |
| Mobile presentation | Stable 30 FPS target with responsive controls | Physical-device large-text/touch and thermal test |
| Common warm interpretation | p95 at or below 3 seconds on nominated desktop baseline | Supported command corpus, realistic context, game active |
| UI feedback | Immediate pending/cancel feedback without waiting for inference | Input-to-feedback trace and cancellation race tests |
| Simulation | Yield to UI in bounded chunks without changing results | Scenario-specific scheduler work/time and determinism checks |
| Saves | Responsive consistent checkpoints and successful recovery | Measured latency/size, disk-full and suspension behavior |
| Long campaign | Initial soak of 100 seeds across 50 simulated years | Accounting/history/memory growth reports; expand after failures |

Targets can be revised with evidence and a documented tradeoff. Do not weaken simulation rules silently to make a device score pass.

## Device matrix

Qualify Windows x64 as first proof; plan Linux/macOS where product scope supports them and Android/iOS mobile spikes early. Each row in the future device registry needs CPU/GPU/RAM/storage, driver/OS, runtime backend, model artifact, context limit, frame target and suspension/thermal results. Emulator success does not replace physical mobile results.

Do not treat a quantized model's file size as the application's total memory. Include runtime/KV caches, game state, graphics/audio, content caches and OS headroom. Enhanced language packs can raise hardware needs without changing world mechanics.

## Workload families

Measure crossing physics/actions, crowded investigation projections, multiple NPC planners, regional shipments, large event bursts, construction, long-time catch-up, save/migration and simultaneous inference. Include cold startup, model reload, long sessions, low storage and background/resume.

Track active/persisted entity counts, schedule queue size, per-domain update cost, projection build cost, replay window growth and content footprint. Coarse simulation transitions preserve defined invariants and the campaign policy; they are not a hidden adaptive difficulty system.

## Failure and release policy

Unsupported hardware produces a clear capability check and recovery options, not a promise that all devices run the same model. A missing required qualification leaves release support unclaimed. Investigate p95 stalls, memory leaks and thermal collapse before enlarging content scale. Release notes identify tested configurations and known limitations.
