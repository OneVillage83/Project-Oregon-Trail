# Clearwater integrated vertical slice

Version 0.2 | Proposed test setting, not a final historical/world-setting decision

## Purpose

Demonstrate creative action, observer-dependent investigation, systemic consequences, and persistent development in one connected world. Clearwater is a fixture name. It does not assert a real-world town, date, geography, or cultural depiction.

The initial workload hypothesis is three connected settlements, a river corridor, woodland route, farm, store/workshop and one investigation interior; six to eight party members and approximately 30–60 named NPCs, with small aggregated populations. Numbers are content estimates to test, not engine capacity claims.

## Starting situation

A party needs to move supplies across a river before a known commitment expires. Its wagon is imperfectly maintained; party members differ in observation, craft, medical, and social skills. The crossing connects trade routes supplying a settlement that wants to improve a building or bridge. A later case involves one of those supply networks. Do not force the player to commit a crime or accept a detective profession to continue.

The fixture must fix terrain, flow direction, routes, weather state, relevant inventories, ownership, commitments, and relevant building geometry before dependent actions. Hidden event history is stored in a developer-only case record. Player views contain only allowed observations and reports.

## Experience A: crossing

Supported approaches include negotiating passage, scouting a safer route, repairing transport, constructing a raft, or engineering another solution from supported physical affordances. At least three materially distinct approaches must be demonstrated. Each consumes actual time/resources and has interruptions and credible failure states.

The barrel-assisted wagon example is a test of containment, sealing, displaced volume, load, attachments, construction skill and uncertainty. It is not a hard-coded success trigger. Thomas's estimate is derived from his measurements and knowledge; the simulation can know a hidden defect he has not detected.

Acceptance: an overloaded design fails or is assessed as unsafe for relevant reasons; unloading changes the relevant calculation; unavailable labor/tools block work rather than appearing from nowhere; a canceled plan retains completed work; save/reload mid-plan continues without duplicating cargo.

## Experience B: investigation

A precommitted event creates physical traces and witnesses. The hunter can notice track features, a carpenter can measure a spatial inconsistency, and a medical observer can identify distinct bodily evidence. Not every observer receives every clue. An observation is not automatically a true accusation.

The player can preserve or disturb evidence, ask limited-knowledge witnesses, compare observations and test a hypothesis. Material ambiguity in targets is clarified. A false claim remains a report/belief, not world truth. The player may reach an incorrect conclusion; the system tracks evidence, institutional decisions and later contradictions.

Acceptance: no model decides the culprit; the accessible view and tooltips cannot reveal the hidden case record; repeating Perception Mode without changed conditions does not reroll indefinitely; reputation reaches another town only through a delivery channel and can generate a contextual request there.

## Experience C: changing settlement

A project requires design knowledge, land/permission, financing, materials, labor, production capacity and time. Resource deficits block it. Work updates a persistent site and later changes the same building's appearance and capabilities. Weather, trade or a workforce interruption can delay completion.

Acceptance: timber-to-brick is an actual construction change, not a global era texture switch; the place and parcel retain identities; ownership and a named bridge or landmark persist through a time advance; maintenance and replacement can change the structure while preserving history. A second fixture exercises a later transport/material capability to prove that the design is not permanently limited to the opening era.

## Player journey and presentation

The opening teaches selection plus language, uncertainty, time commitment and cancellation. Use a persistent command field, central map/scene and collapsible Party, Inventory, Journal, Camp and Reports panels. Provide a concise action interpretation before expensive or irreversible plans. Completed events expose a brief result, known costs, and an expandable observer-safe explanation.

Do not put a glowing marker on every meaningful object. Detection may reveal restrained labels or overlays. Keyboard and touch paths must reach the same information as mouse use. An accessible scene description must not bypass perception.

## Integration proof, not isolated demos

The same cargo, people, routes, laws and construction ledger participate in all experiences. Route damage can delay materials; the resulting shortage can change price and employment; a witness's travel controls when a case report arrives. Shared IDs, event records and saves must connect these effects.

## Exit review

Use the SC-CROSS, SC-CASE, SC-TOWN and SC-CONTINUITY scenarios in the [acceptance catalog](../quality/SCENARIO_ACCEPTANCE_CATALOG.md). Run each through structured input first, then the model. Test multiple seeds where the fixture supports generation, and retain authored deterministic fixtures for regression. Record playtest comprehension, failed commands, discoverability, pacing and whether alternative solutions were genuinely understandable. Passing one rehearsed developer walkthrough is insufficient.
