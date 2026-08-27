# World Simulation and Generation

## Objective

The campaign world should be generated as an objective, persistent reality that exists independently of what the player has discovered.

Exploration reveals the world; it does not cause the narrative model to invent it on demand.

## Seeded generation

A campaign begins with a world seed. The seed establishes the initial geography and foundational simulation state.

Potential generated systems include:

- terrain;
- elevation;
- watersheds and rivers;
- forests;
- plains;
- deserts;
- mountains;
- swamps;
- resource deposits;
- wildlife populations;
- settlements;
- roads and trails;
- political territories;
- trade networks;
- ruins;
- caves;
- institutions;
- demographic distributions.

The player may initially know only a very small portion of this state.

## Spatial hierarchy

A useful hierarchy is:

`World -> Region/Chunk -> Local Area -> Scene -> Object`

### World
Large-scale geography, climate, civilization, and long-range networks.

### Region / Chunk
A simulation and persistence partition containing local terrain, routes, populations, resources, and settlements.

### Local Area
The player's immediate geographic location, such as a river crossing, forest clearing, town block, farm, roadside camp, or building site.

### Scene
A rendered or interaction-relevant spatial instance.

### Object
An individual simulated entity with identity, state, properties, and affordances.

## Discovery state

The simulation must distinguish:

- objective existence;
- world knowledge held by NPCs/institutions;
- player-party knowledge;
- map knowledge;
- rumors;
- hypotheses;
- stale information.

A gold deposit can exist without the player knowing it exists. A town can be known by rumor but not mapped accurately. A road can move or deteriorate after the player's map information becomes outdated.

## Persistent local state

If a player changes a scene, that change persists unless later simulation changes it again.

Examples:

- a rug remains moved;
- a chair remains broken;
- a secret bookshelf remains open;
- a bridge remains damaged;
- a campfire consumes fuel;
- a building burns down;
- a road becomes washed out;
- a shop changes inventory;
- a settlement expands.

Seeded generation establishes reproducibility, but mutable simulation state must be stored separately from the seed.

## Scene instantiation on demand

Not all buildings and rooms need full spatial rendering from the beginning.

A location may exist abstractly until a gameplay event requires higher detail.

Example merchant:

```text
owner = Elias Cooper
location = Clearwater
building = general store
inventory = 176 items
quality = modest
```

Routine trade may use portrait/background UI.

If a murder occurs inside the store, the simulation can instantiate a detailed scene containing:

- room dimensions;
- doors;
- windows;
- counter;
- shelves;
- furniture;
- object placement;
- body position;
- evidence;
- lighting;
- hidden state.

Once instantiated and materially interacted with, that scene becomes persistent.

## Simulation layers

The long-term world is expected to include interacting systems such as:

- population and family;
- psychology and goals;
- relationships and factions;
- health, injury, disease, nutrition, and medicine;
- ecology and wildlife;
- climate and weather;
- economy, production, supply, demand, and trade;
- materials and items;
- crafting and construction;
- knowledge, education, research, and technology;
- law, crime, reputation, and politics;
- transportation and infrastructure;
- historical memory and information propagation.

The value comes from interactions between these systems, not from treating them as isolated minigames.

## Information propagation

Stories and reputation should spread through actual channels where practical:

- witnesses;
- travelers;
- merchants;
- letters;
- newspapers;
- telegraph;
- radio;
- telephone;
- later communication technologies.

This allows a character's reputation to move through the world rather than becoming globally known instantly.

## Example emergent detective arc

1. A hunter has high perception and tracking skill.
2. A murder occurs in a settlement.
3. The player investigates using those abilities.
4. The case is solved.
5. Witnesses and newspapers propagate the story.
6. The character gains investigation experience and reputation.
7. Another settlement hears the story.
8. An NPC later seeks that character out to investigate a disappearance.

No predefined detective class or detective campaign is required.

## Economy and physical world interaction

Economic state should be connected to production and logistics.

Weather may damage roads, which delays merchants, which reduces supply, which increases prices, which may create shortages, migration, crime, or new investment opportunities.

The purpose is systemic causality.

## Technological aging

Technology should progress through knowledge, institutions, resources, infrastructure, production capacity, and adoption rather than cosmetic era switching.

A settlement may evolve through:

- timber construction;
- brick/masonry;
- industrial materials;
- steel infrastructure;
- electrical systems;
- automobiles;
- plastics;
- telecommunications;
- computing;
- later technologies.

Transportation, communication, medicine, construction, manufacturing, policing, commerce, and warfare all change as technology develops.

## Geographic continuity

The same place should remain recognizable through time even when transformed.

Example Clearwater Crossing:

- Year 1: river crossing, ferry, several timber structures;
- Year 30: established settlement, bridge, shops;
- Year 60: brick commercial district and rail connection;
- Year 100: paved roads, automobiles, electric infrastructure;
- later: additional urban growth.

A player-built bridge may become a named landmark. If replaced, its name or historical significance may survive.

## Performance strategy

The game does not need to simulate every entity at identical temporal resolution.

Long-term architecture should support multiple simulation granularities:

- high fidelity around the active player and consequential events;
- scheduled/event-driven simulation for nearby entities;
- aggregated simulation for distant populations/economies;
- deterministic reconstruction where appropriate.

This is essential for large persistent worlds and mobile feasibility.

## World history

Authoritative world events should form a historical record that can influence:

- reputation;
- biographies;
- newspapers;
- institutional memory;
- location names;
- monuments;
- inherited wealth;
- family relationships;
- political narratives;
- future opportunities.

The world should become increasingly unique because of what actually occurred during the campaign.
