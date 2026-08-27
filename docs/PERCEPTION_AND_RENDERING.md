# Perception and Rendering Architecture

## Purpose

The visual layer must help the player reason about the simulated world without forcing the game into expensive 3D production or cluttering every scene with highlighted interactables.

The central rule is:

> **The simulation determines what exists. The renderer determines what can be shown. Perception determines what the observing character actually notices.**

## Perception Mode

The inspection feature is called **Perception Mode**.

Perception Mode does not reveal every possible interaction. It exposes details the active observer is capable of noticing based on stats, experience, environmental conditions, attention, and domain knowledge.

### Example room truth

A room might objectively contain:

- bookshelf;
- hidden book lever;
- floor scratches near the shelf;
- faint draft behind the shelf;
- blood droplet beneath a desk;
- knife on the table;
- mud on the windowsill;
- fingerprint on glass;
- recently extinguished candle;
- loose floorboard.

A low-perception character might only notice the obvious furniture and knife.

A hunter may notice mud patterns or tracks.

A carpenter may notice that the bookshelf has repeatedly moved or that room dimensions do not match the building.

A physician may notice bodily evidence others miss.

A trained investigator may notice combinations of evidence and inconsistencies.

## Perception model

A first-pass conceptual formula is:

`Detection = General Perception + Relevant Skill + Familiarity + Attention + Environmental Modifiers - Concealment Difficulty`

Relevant modifiers may include:

- lighting;
- distance;
- fatigue;
- distraction;
- weather;
- injury;
- time spent searching;
- clue salience;
- object familiarity;
- profession-specific knowledge.

General perception should therefore not replace domain expertise.

## Perception progression

Perception and related observational skills improve through use and experience.

A hunter who spends years tracking animals may naturally become an unusually capable observer. If that person later solves crimes, improves interviewing and deduction, and develops a reputation, the world may begin treating that person as a detective without a predefined class transition.

This progression can lead to emergent careers and storylines.

## Scene rendering strategy

Ordinary world visuals should be created through **modular 2D scene composition**, not live image generation.

The renderer consumes structured scene state such as:

```text
terrain = muddy_riverbank
river_flow = west_to_east
forest_density = heavy_northwest
wagons = 2
horses = 4
campfire = active
rain = heavy
Jacob.location = upstream_scout_route
Sarah.activity = resting
```

It then assembles the scene from authored assets.

## Directional consistency

Major directional assets should support enough orientations that visual direction matches simulation state.

Typical orientation set:

- N
- NE
- E
- SE
- S
- SW
- W
- NW

Likely candidates include:

- wagons;
- horses;
- characters;
- boats;
- cars;
- carts;
- chairs;
- weapons;
- machinery.

If upstream is to the left on a local map, the river geometry and directional indicators must agree.

## Stateful objects

Animation is optional; state representation is not.

A secret-lever book may have:

```text
STATE_0 = seated normally
STATE_1 = partially pulled
STATE_2 = removed
```

A bookshelf may have:

```text
STATE_0 = closed
STATE_1 = mechanism triggered
STATE_2 = shifted/open
```

The renderer swaps or composes the appropriate art state after the simulation changes the object.

## Rendering levels

Not every location deserves the same visual budget.

### Level 0 - Unknown
No detailed rendering.

### Level 1 - Strategic map representation
Town, road, landmark, region, route, or point-of-interest icon.

### Level 2 - Context interaction
Portrait + contextual background + specialized UI. Suitable for routine merchant interactions, ordinary conversations, administration, and other cases where exact spatial layout is irrelevant.

### Level 3 - Full local scene
Detailed 2D scene where spatial relationships matter.

### Level 4 - Investigation / event scene
Interactive scene with evidence, object state, meaningful placement, and Perception Mode.

### Level 5 - Focus view
Close inspection of an object, wound, mechanism, document, machine, clue, or other detailed target.

Locations may move between levels when gameplay demands it. A merchant shop can remain Level 2 for years and become Level 4 after a murder or other spatially important event.

## Visual clues

The game should avoid both extremes:

- clues invisible unless the player guesses a specific command;
- every meaningful object glowing obviously.

Instead, scenes should communicate anomalies through restrained visual information:

- different book colors;
- dust differences;
- scuff marks;
- crooked rugs;
- mismatched construction;
- displaced objects;
- stains;
- footprints;
- damaged vegetation;
- lighting differences;
- subtle gaps or drafts when perception permits.

Perception Mode may add restrained overlays or labels only after detection.

## Interaction with natural language

Visual selection and language should cooperate.

Example:

1. Player taps a bookshelf.
2. UI stores `selected_entity = bookshelf_1842`.
3. Player types: "Check behind this."
4. Language parser resolves `this` to the selected entity.
5. WALang receives a precise target reference.

This reduces ambiguity and lowers the burden on the local language model.

## UI behavior

Major panels such as Party, Inventory, Map, Camp, Journal, and Reports should be:

- collapsible;
- expandable;
- pinnable where useful;
- compatible with a large central world view.

The user should be able to switch naturally between information-heavy management and a mostly unobstructed scene.

The natural-language command field remains available across major interface contexts, including:

- travel;
- camp;
- trade;
- inventory;
- investigation;
- character management;
- combat;
- workshop/crafting;
- medical interaction.

## Historical visual change

Visual assets must support world aging.

Settlements and infrastructure can transition through eras:

- wood construction;
- masonry/brick;
- steel;
- industrial infrastructure;
- electrical infrastructure;
- plastics and modern materials;
- automobiles;
- later technologies.

This is not merely a cosmetic skin. Visual change should correspond to real technological, economic, and infrastructural state in the simulation.
