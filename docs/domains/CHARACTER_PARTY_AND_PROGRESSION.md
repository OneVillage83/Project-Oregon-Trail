# Characters, party control and progression

Version 0.2 | Owner: gameplay lead | Requirements PR-005/006/015/019

## Owned state and boundaries

Character records own identity, age/lifecycle, baseline attributes, acquired skills, experience provenance, personality preferences, needs and social-role references. Health owns diagnoses/injuries; Knowledge owns observations/beliefs; Property owns inventories/titles. Character records reference these rather than duplicating their truth.

Party records own membership, leadership/delegation permissions, shared resources, current commitments, planned destinations and observer selection. An active observer is a character with a perspective, not an omniscient camera. The player may see shared known information but does not automatically learn what an isolated scout just discovered.

## Attributes and skills

Use a small general-attribute set for initial implementation: physical capability, endurance, coordination, general perception and cognitive/social learning capacities. Exact names/ranges remain versioned balance data. Domain skills include tracking, construction, medicine, negotiation, investigation and later technological practices. General perception cannot replace domain expertise.

Skill records contain proficiency, relevant practice events, learning context, fatigue constraints and meaningful challenge history. Repetitive trivial actions have diminishing or zero gains. Teaching, tools, deliberate practice, failures and new situations can contribute according to explicit progression rules. Models do not award experience.

## Emergent occupations

An occupation is an observed social role/reputation plus capabilities and institutional permissions, not a mandatory class choice. A hunter can learn investigation and earn requests through actual cases and communicated achievements. Changing a displayed role does not grant tools, knowledge, authority or hidden bonuses.

Initial biographies provide varied prior experience without making future actions inaccessible solely by class. Cultural/demographic identity is not a blanket proxy for ability. Any historical qualifications or social restrictions belong in reviewed setting content and institutional rules, not unexplained engine constants.

## Party authority and consent

Membership does not imply unlimited control. Define authority for resource use, spending, task assignment and risk; independent actors may refuse. The player can ask, negotiate, hire or lead. Orders beyond authority become requests. A character who owns a horse does not lose ownership merely because the party inventory panel shows it.

Splitting the party creates separately scheduled actors/locations and knowledge. Communication reunites reports. Switching observer cannot teleport actors or synchronously know remote secrets. A remote assignment is delivered through an actual channel where required.

## Needs, morale and lifecycle

Needs consume time/resources and influence attention and task performance through documented modifiers. Morale relates to events, relationships, goals and conditions, not arbitrary invisible punishment. Use bounded effects and expose actor-permitted explanations. Injury and fatigue can interrupt tasks; death/retirement trigger cancellation, property and succession workflows.

Births, adoption and kinship are relationship/lifecycle events with stable identity. Family continuity does not require explicit reproductive content. Inheritance is handled by the law/property layer, while the continuity UI offers valid successors. Disability/care and aging are represented through capabilities and accommodations rather than deleting agency automatically.

## Events and interfaces

Consume TaskProgressed, PracticeQualified, ObservationAcquired, HealthStateChanged, AgreementAccepted and LifecycleChanged. Emit SkillProgressed, RoleRecognized, PartyMembershipChanged, AuthorityChanged and CharacterRetired/Died. These are planned semantic event names; each must acquire a typed schema before implementation. Event names in domain documents do not imply currently registered runtime support.

## Acceptance

SC-PROGRESSION proves meaningful practice and diminishing repetition; hunter-to-investigator identity requires actual ability and reputation. SC-PARTY tests split-party knowledge, resource authority, refusal, observer changes and actor loss mid-task. SC-CONTINUITY tests death/retirement without duplicated property or orphaned orders. Save all skill and authority provenance required to reconstruct consequential changes.
