# Core Design Principles

These principles are architectural constraints for Project Oregon Trail. Systems should be evaluated against them before implementation.

## 1. Simulate actions, not spectacle

The project prioritizes interaction depth, simulation fidelity, and emergent consequences over expensive 3D rendering or animation.

The center world view is not decorative. It must represent real simulation state closely enough that players can reason from what they see.

## 2. The simulation determines what exists

World state must originate in deterministic or rule-driven simulation systems.

The simulation defines:

- geography;
- people;
- objects;
- inventories;
- injuries and diseases;
- economies;
- weather;
- relationships;
- knowledge;
- clues;
- technologies;
- historical events;
- spatial relationships.

Narrative models and renderers consume that state. They do not invent replacements for it.

## 3. The renderer determines what is visually presented

Visual presentation should be generated from world data using authored modular 2D assets, layered composition, object states, directional variants, environmental overlays, and scene templates.

Do not rely on live generative-image APIs for ordinary world rendering.

## 4. Perception determines what an observer notices

The world may contain more information than any given character can detect.

The rendering and narration layers receive only information that the active observer has legitimately noticed, learned, inferred, or otherwise acquired.

The separation is:

> **World truth -> observable state -> perceived/known state -> player presentation**

## 5. Natural language is the freedom layer

The persistent command line is the primary mechanism for expressing actions that would be impractical to enumerate as buttons.

Traditional menus remain available for common operations where they are faster and clearer.

## 6. AI interprets; simulation resolves

Local AI may translate natural language to structured intent and translate simulation output to prose.

It may not directly determine success, create evidence, alter authoritative state, or reveal unknown facts.

## 7. Failure should be systemic

Valid actions may fail because of:

- insufficient skill;
- missing tools;
- bad luck where randomness is appropriate;
- physical limits;
- social resistance;
- environmental conditions;
- incomplete information;
- interruptions;
- poor planning.

The game should distinguish parsing failures, validation failures, and genuine simulation failures.

## 8. Player creativity is not an error case

When the player proposes an unusual method, the system should attempt to decompose it into reusable actions, materials, properties, constraints, and goals instead of rejecting it merely because no bespoke button exists.

Example: a rifle barrel used as a lever should be evaluated as an object with geometry, strength, condition, and lever-like use—not require a hard-coded `USE_RIFLE_AS_LEVER` command.

## 9. Objects should be meaningful entities

Visible objects should correspond to actual simulation entities wherever gameplay may depend on them.

A bookshelf rendered in an investigation scene should have an object identity, location, contents, material, condition, affordances, and possibly hidden state. It is not merely background art.

## 10. Visual consistency is gameplay information

If a river flows west to east, the rendered river should visually reflect that geometry. If a wagon faces northeast, its visual orientation should match.

Once visuals convey game information, incorrect art placement becomes misinformation.

## 11. Render detail only when gameplay requires it

Not every location needs a fully interactive scene.

A normal merchant transaction may use:

- character portrait;
- contextual shop/cart background;
- inventory/trade panels;
- persistent command input.

A crime scene, engineering problem, combat encounter, or spatial puzzle may instantiate a detailed interactive scene.

## 12. Worlds are generated before discovery

The campaign seed creates an objective world that exists independently of player knowledge.

The player discovers that world over time. Exploration reveals pre-existing geography and entities rather than causing the narrative model to invent whatever is needed at the moment.

## 13. The world persists and ages

Objects, settlements, roads, institutions, technologies, family histories, reputations, and built structures should evolve rather than reset between visits.

Changes should accumulate into history.

## 14. Professions and stories emerge from behavior

Characters become hunters, physicians, traders, detectives, criminals, leaders, engineers, or other roles because of what they repeatedly do, learn, and become known for.

The game should prefer emergent identity over rigid class selection.

## 15. Knowledge is a resource

The simulation must distinguish objective truth from what each actor knows, believes, suspects, remembers, or has been told.

NPC dialogue is constrained by NPC knowledge.

## 16. Touch, mouse, text, and voice should cooperate

A player may select an object visually and then say or type "check behind this." Visual selection supplies a precise entity reference; natural language supplies the action and intent.

## 17. The language model is replaceable

Game architecture must not depend on one vendor or one specific model family. The natural-language layer must be replaceable as local-model technology improves.

## 18. Offline play is a first-class requirement

The baseline game must not require permanent external inference services, subscriptions, or per-token usage.

## 19. Mobile should remain possible without lowering simulation integrity

Rendering and language-model tiers may scale with hardware, but world mechanics and authoritative simulation rules should remain consistent across platforms wherever feasible.

## 20. Debuggability is mandatory

For any consequential action the system should be able to reconstruct:

`Natural input -> parsed intent -> resolved references -> validated execution plan -> simulation events -> state changes -> presentation`

This traceability is essential for QA, replay, balancing, and trustworthy AI-assisted interaction.
