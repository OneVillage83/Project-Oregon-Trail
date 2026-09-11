# Client, rendering and input contracts

Version 0.2 | Owner: client/UX lead

## Ownership

The client presents the world without becoming a second simulation. Actionable visible objects correspond to entities; purely decorative elements are explicitly noninteractive. UI actions submit intents and await receipts. Client state contains ObserverView, selection/discourse, pending interpretations, public tasks and layout preferences—not hidden truth.

## Layout and interaction

Keep a persistent command field across travel, camp, trade, inventory, investigation, crafting, care and management. Party, Inventory, Map, Camp, Journal and Reports are collapsible/expandable and optionally pinnable. A selected object plus 'check behind this' resolves to a supplied view token. Mouse, keyboard, touch and optional local speech share the same input envelope.

Support editable drafts, command history, selected-target chips, an explicit active observer and clear time status. Speech is editable before costly action. Virtual keyboards must not cover preview/confirmation. Routine inventory work should not require lengthy generated dialogue.

## Interaction state machine

Idle → composing → interpreting → clarification/preview → submitted → running → result. Canceling an unaccepted interpretation invalidates its request. Canceling an accepted plan is a separate simulation action and preserves completed work. Material changes to observer/scene/references invalidate or revalidate previews.

Show interpreted actors, targets, quantities, hard limits, estimated duration and irreversible steps. Unknown cost is not zero cost. Use observer-known estimates, not hidden exact success probabilities. Parsing, infrastructure, unsupported mechanics and attempted-action failure have different messages.

## Rendering levels

Retain unknown, strategic map, contextual interaction, local scene, investigation and focus views. A portrait-based shop can have exact stock without rendered geometry. Relevant interiors are fixed before dependent events. View-level changes do not rewrite facts.

Compose terrain, buildings/props, characters/equipment, material/state variants and environmental overlays. Orientation, attachments, river flow, occupancy and access derive from shared geometry. Cosmetic interpolation cannot assert that someone crossed a blocked route or opened a closed object.

## Perception presentation

Perception Mode asks for the observer's permitted observations. Obvious objects remain readable; subtle details acquire overlays only after detection. Avoid universal glowing clues. Mode toggling does not reroll detection without a new valid examination.

Tooltips, names, suggestions, accessible labels and audio cues follow the same projection. Assets themselves must not reveal hidden state accidentally: a unique secret-door texture must not identify a concealed door unless that irregularity is an intended observable clue. Caches include observer and knowledge revisions.

## Results and failure behavior

Committed events drive exact concise results, inventory/task changes, journals and optional narration. Show completed steps, known costs and next decisions. Group event bursts without dropping consequential facts. A long task shows partial progress and interruptions.

Rendering/audio failures do not mutate the world. Missing cosmetic assets use neutral fallbacks. Missing gameplay-critical states block a pack or use a validated schematic view. Never depict an intact bridge when it is destroyed.

## Performance and accessibility

Rendering/UI budgets are independent of simulation and inference. Build scalable text, keyboard focus, remapping, readable contrast, reduced motion, subtitles and non-color-only signals. Accessible descriptions convey the same known information. See [accessibility](../content/ACCESSIBILITY_LOCALIZATION_AND_TUTORIAL.md).

SC-UI covers selection/pronouns, stale previews, cancel races, menu/text equivalence and small screens. SC-VISUAL covers direction, object/era state and observer-safe assets. SC-ACCESS compares keyboard/touch/accessibility paths. Temporary art is acceptable in early proofs; temporary competing world logic is not.
