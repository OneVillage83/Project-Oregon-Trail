# Emergent situations, requests and story opportunities

Version 0.2 | Owner: gameplay/world-systems lead | Requirements PR-006/010/015/017

## Purpose

Turn actual unmet needs, conflicts, discoveries and communicated reputations into understandable player opportunities. This is not an omniscient quest generator that invents facts to maintain dramatic pacing. The world continues to behave consistently when the player declines an opportunity.

## Ownership and inputs

The situation registry owns opportunity identity, originating need/event, eligible participants, contact channel, visibility, offer status, deadlines and resolution references. It consumes domain facts and permitted knowledge; it does not own inventories, crimes, NPC relationships or technology.

Examples include a damaged route requiring repair, a merchant seeking a shipment, a patient needing care, an institution funding a school, an unsolved case, or a settlement that has heard of an investigator. Each situation must have an actual source and a credible actor or institution able to make the request.

## Lifecycle

Potential situation → domain-validated need → eligible requester/offer → communication/contact → known opportunity → accepted commitment or declined/expired request → ongoing work → resolved/failed/superseded. Acceptance creates an ordinary agreement, work order or authorized plan. It does not activate a separate set of physics or instant rewards.

Store source event, requester, beneficiary, known facts, task/goal predicate, available budget/resources, deadline, contact path, eligibility rules and supersession conditions. An offer cannot promise funds the requester does not possess or explicitly borrow. A character receives a distant request only after communication delivery.

## Causal integrity

Do not choose a culprit, hidden location or scarce item after the player accepts a quest. Commit relevant facts before dependent events. A case can remain unsolved; a request can become obsolete because another NPC acts; a bridge may be repaired without the player. Resolve those changes through the same world events and update contacts rather than leaving stale mandatory quest markers.

The player's reputation is learned through actual reports with source ancestry. Eligibility cannot read a private character class, undiscovered clue or future success probability. A hunter becomes eligible for investigator work through known achievements and capability signals, not an arbitrary campaign-mode switch.

## Opportunity selection and pacing

A presentation broker can rank opportunities already known to the observer by urgency, relevance, travel cost, user preferences and notification budgets. It may group repetitive offers, apply per-source cooldowns or hide low-priority notifications without deleting their underlying world needs. Pacing controls delivery/presentation, not whether a storm or crime secretly occurs to produce entertainment.

Use bounded situation scans and event subscriptions. Avoid creating one request per resident per tick. Aggregate similar institutional needs and retain individual commitments where consequential. Duplicate detection keys include source event/need, requester and goal; a reload cannot issue the same reward twice.

## Content templates and language

Templates define supported need predicates, legal offer terms, permitted explanation slots, contact options and resolution references. They do not contain unrestricted scripts that set success. A language model can phrase the request from its fact bundle; the exact terms remain structured. Optional narrative summaries link to committed event history and cannot fabricate achievements.

Authored scenarios may seed starting conditions as declared scenario inputs. This is different from silently rewriting a live campaign. Every seed event and special scenario rule belongs in its manifest and replay provenance.

## Persistence and failure

Persist active situations, outstanding contacts, accepted agreements, reward transfers and resolution IDs. Source invalidation cancels or supersedes the offer with an appropriate communication event. Lost requester authority, budget exhaustion and unreachable destinations produce explicit states, not automatic failure blamed on the player.

## Acceptance

SC-REGIONAL proves a shortage creates a funded, deliverable opportunity through actual logistics. SC-COMMUNICATION proves distant requests wait for knowledge and contact. SC-CASE proves the underlying mystery is fixed and survives rejection/reload. SC-INSTITUTION proves a project offer uses real authority and budget. Add specific request-generation fixtures to B-019/B-021/B-023/B-024 before those features are marked complete.
