# Project Vision

## Working concept

Project Oregon Trail is a simulation-first game built around a simple principle:

> **Do not spend the complexity budget primarily on what the player sees. Spend it on what the player can do and how the world can respond.**

The game takes inspiration from the structural accessibility of *The Oregon Trail*, but greatly expands player agency, world simulation, character development, economy, disease, crafting, investigation, social systems, technology, and persistent history.

A campaign should be capable of becoming radically different without selecting a predefined game mode. The same simulation may organically become:

- a survival expedition;
- a merchant/trading campaign;
- an outlaw story;
- a medical career;
- an exploration/cartography campaign;
- a settlement-building story;
- an investigation/detective career;
- an industrial or technological progression story;
- a political or organizational simulation;
- a multigenerational world-history campaign.

The objective is not to author thousands of isolated scripted quests. The objective is to create systems that continuously generate meaningful situations through interaction.

## Player interaction philosophy

The primary interaction method is free-form natural language. The persistent command field should allow the player to describe what they want to attempt rather than choose only from predefined dialogue wheels or action buttons.

Examples:

- "Have Jacob scout five miles upstream, but return if the weather gets worse."
- "Measure this room and compare it with the outside dimensions of the building."
- "Offer all three hides for the rifle and forty cartridges, but do not go above another five dollars."
- "Empty the barrels, seal them, strap them underneath the wagon, unload everything except food and medicine, and ask Thomas whether he thinks it will float."

Traditional UI remains available where it is more convenient: inventory, party management, map, journal, trading, character sheets, equipment, and contextual object selection. Natural language provides freedom; conventional UI provides efficiency.

## Simulation authority

The simulation is always authoritative.

Local language models may:

- interpret player language;
- resolve likely semantic intent;
- express NPC dialogue;
- transform simulation events into readable prose.

They may not:

- invent world state;
- create outcomes;
- alter inventory directly;
- decide physical success or failure;
- reveal information an actor does not know;
- bypass simulation rules.

The core architecture is therefore:

`Player Language -> World Action Language -> Validation -> Simulation -> World Events -> Rendering/Narration`

## Emergent identity and professions

Characters do not need fixed classes. Skills and reputation should emerge from repeated behavior and experience.

A hunter may develop exceptional perception through years of tracking. That character might later solve a local crime, build investigation experience, gain a reputation, and eventually become known throughout the region as a detective. Other characters may then seek that person out for cases.

The world should react to what a character becomes rather than require the player to select a class in advance.

## Persistent history

Player actions and simulation events should become world history.

A bridge built in an early campaign year may later become a named landmark. A small trading post may become a city. A character's actions may appear in newspapers, stories, institutional names, family histories, or local folklore decades later.

The world should remember enough that returning to the same place generations later feels like revisiting a place with actual history rather than loading a replacement scene.

## Long-duration technological change

The world is expected to age.

Settlements should be capable of progressing from wood construction to brick, steel, plastics, automobiles, electrical infrastructure, telecommunications, computers, and later technologies if the simulation reaches those periods.

Technological change must affect both presentation and mechanics. A road may evolve from a wagon trail to a graded road, paved road, and highway. Communication may evolve from courier and letter to telegraph, telephone, radio, and later systems.

The same underlying world geography should persist while infrastructure and society transform over time.

## Platform philosophy

The game should be architected so the core simulation can run across PC and mobile where practical. Graphics should remain intentionally lightweight enough that hardware resources can be devoted to simulation and local language processing.

A PC version may support larger local models or higher simulation density, but the game's fundamental rules should not depend on cloud AI services.

## Offline-first requirement

A core product goal is that the game remain playable with external servers unavailable.

No required recurring AI API cost should be necessary after distribution. Local models, procedural systems, deterministic simulation, and local persistence should provide the complete baseline experience.
