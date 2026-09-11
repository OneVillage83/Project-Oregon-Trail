# Art, audio and asset production pipeline

Version 0.2 | Owner: technical-art/content lead

## Visual strategy

Use authored modular 2D composition consistent with the foundation. No live image-generation API is required for world rendering. Development-time generated assets, where used, need provenance, licensing review, art-direction consistency and state coverage. The game must still render offline.

Define an art bible before volume production: perspective/camera conventions, scale, palette, readability, materials, light/weather layers, animation economy, UI typography and historical/fictional setting constraints. Final aesthetic/setting choices require product review; do not treat placeholder fixture art as approved branding.

## Asset manifest

Every gameplay-relevant family records asset ID, corresponding prototype/component states, supported directions, anchors, bounds, interaction silhouette, layering/z-order, material variants, damage/open/closed states, era/capability applicability, localization/accessibility hooks, provenance and license.

Use a canonical eight-direction set where direction matters, but allow validated reduced variants for symmetric assets. Reflection is not always valid for handed mechanisms or asymmetrical equipment. River flow and building access must match simulation geometry.

## Control combinatorics

Compose clothing, equipment, material, weather and damage overlays rather than duplicating every full image. Define required state combinations and forbidden combinations. An eight-direction vehicle with three damage states already has 24 directional-state cases before materials; manifest coverage should be reviewed before producing variants.

Assets need not animate every action. A consistent state change is more important than an elaborate animation that contradicts the world. Focus views can explain a mechanism or condition when exact spatial detail is relevant.

## Pipeline stages

Concept/reference approval → prototype/blockout → state/anchor validation → production art → import/compression → in-engine scene test → observer/era review → license/provenance approval → pack compilation. Preserve source files and exported runtime assets with reproducible import settings.

Missing cosmetic variation may use a neutral fallback. Missing gameplay-significant state must block the pack or use a validated schematic presentation; never show intact equipment after destruction. Track art debt by required manifest states, not only file counts.

## Audio

Audio conveys environmental ambience, task feedback and significant events without revealing hidden facts. Spatial/audio clues pass the same observation policy. Music and ambient variation are cosmetic and use a separate nonauthoritative random stream. Voice is optional and must not delay exact critical UI. Provide subtitles, separate volume channels, mute controls and reduced-intensity presentation options as appropriate.

Record performer/voice/license provenance. Do not silently use an unlicensed cloned voice or a model's training-license assumptions as permission to distribute an audio asset. Generated speech must express the committed speech act; its wording cannot change terms.

## Quality and acceptance

SC-VISUAL checks state/direction, occlusion, anchors, readable evidence and mixed-era scenes. SC-ACCESS checks non-color cues, captions and perception-equivalent audio descriptions. Validate peak texture/audio memory on nominated devices and budget streaming/import formats accordingly. Technical art signs off state coverage before a gameplay scenario is marked presentation-complete.
