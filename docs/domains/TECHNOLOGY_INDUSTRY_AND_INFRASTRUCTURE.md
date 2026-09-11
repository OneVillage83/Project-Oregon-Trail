# Technology, industry and evolving infrastructure

Version 0.2 | Owner: technology/content-systems lead | Requirement PR-018

## Required destination

The world can progress from timber settlements to masonry/brick, industrial structures, electricity, vehicles, modern materials including plastics, telecommunications, computing and later technologies. This is mechanical and visual development at persistent locations, not a global cosmetic era switch. An early brick-building test does not remove later systems from the architecture.

## Technology lifecycle

Separate discovery, documented knowledge, transmission, trained workforce, process capability, resources/equipment, production, affordability, adoption, maintenance and obsolescence. A town can know about a technology without having the facilities or supply chain to use it. Old and new systems can coexist; places advance at different rates and may decline.

A technology definition contains ID/version, knowledge prerequisites, process/capability prerequisites, resource/facility requirements, training, infrastructure dependencies, adoption costs, maintenance and affected systems/assets. Use typed prerequisite predicates rather than one unqualified 'era >= 3' test. Validate dependency graphs, permit deliberately modeled alternative paths, and flag unintentional cycles/deadlocks.

## Capability chains

Opening construction chains exercise timber processing, kiln/masonry knowledge, fuel/clay/labor and suitable sites. Industrial chains add machines, energy, skilled labor and logistics. Vehicle adoption requires vehicles/fuel or energy, routes, maintenance, supply and trained operation. Modern-material chains require reviewed feedstock/process/facility abstractions. Telecommunications/computing require equipment, power/service, access and knowledge.

These are deliberately bounded gameplay abstractions, not full industrial engineering recipes. Each introduced process has validity limits and researched content provenance. Do not claim complete real-world production fidelity or let a model create unsupported chemistry/engineering.

## Infrastructure services

Represent roads/rail, transport terminals, power, water, sanitation and communication as persistent networks with nodes/edges, capacity, availability, ownership, maintenance and service demand. Domain solvers can differ, but they share events and accounting. Failure affects connected service and users; it is not merely a damaged texture.

Start with bounded flow/capacity models, not large distributed real-time engineering solvers. Route capacity influences logistics. Power/service availability gates facilities. Communication availability changes information latency/reach. Medicine, construction, policing and commerce consume these actual capabilities.

## Persistent places and assets

Settlement, parcel and site IDs remain stable through rebuilding. Individual structures/vehicles have creation, replacement and destruction histories linked to the site. Asset selection follows actual material/state/capability. Mixed-era scenes are expected. A historical bridge name can survive replacement; its new carrying capacity comes from the replacement structure, not the remembered name.

New technology mostly adds materials, prototypes, processes, skills and affordances. When genuinely new behavior is needed, add a versioned rule module with tests. Do not replace WALang or the save identity scheme every century.

## Progression and content boundaries

A fictional scenario may accelerate research/adoption for testing, but normal play must support understandable investment, teaching, resource acquisition and maintenance. Do not automatically unlock a technology at a calendar year unless an explicitly selected scenario rule calls for it. Never impose a new launch era ceiling without product approval and store-scope disclosure.

## Acceptance

SC-TECH checks missing knowledge, missing factory capacity, unavailable energy, blocked supply and mixed-era adoption. SC-TOWN checks a funded construction upgrade with real outputs. SC-CONTINUITY revisits the same place after advancement and verifies names, ownership, topology and historical facts. Include at least one later transport/material chain in architectural proof; modern systems remain unimplemented until their own qualified content/rules exist.
