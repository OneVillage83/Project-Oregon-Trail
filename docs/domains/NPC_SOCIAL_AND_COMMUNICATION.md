# NPC agency, social interaction and communication

Version 0.2 | Owner: AI-systems/gameplay lead | Requirements PR-010/015/017

## NPC decision architecture

NPCs use utility-based goal selection with bounded hierarchical planning over supported operations. This is a working algorithm choice to test, not a requirement to implement unrestricted general intelligence. An NPC evaluates its needs, goals, resources, relationships, beliefs, commitments and authority. The same validator/scheduler/physics apply to players and NPCs.

Decisions are event-driven or scheduled at appropriate resolution, not a language-model call for every NPC every frame. Candidate goals, planning depth, expansions, time horizon and replanning frequency have explicit budgets. Cache valid plans by relevant state revisions; replan when dependencies change. Repeated infeasible goals back off rather than consume unlimited CPU.

## State

NPC state includes goal priorities, bounded utility inputs, risk preferences, social relationships, outstanding commitments, occupations, legal authority and knowledge references. Keep relationship dimensions separate: trust, familiarity, obligation, fear, affection and professional reputation need not move together. Values are versioned game abstractions, not psychological measurement claims.

## Social operations

ASK, TELL, OFFER, REQUEST, NEGOTIATE, PERSUADE, DECEIVE and ACCUSE have typed semantic content and target/knowledge/authority checks. A proposition can be unknown or false. A threat or persuasion attempt can fail; it does not override ownership or autonomy directly.

The simulation selects a speech act: answer, refuse, warn, counteroffer, deliberate lie or commitment. The model realizes wording from permitted facts. A generated sentence cannot promise a resource that the simulation never authorized. Accepted agreements produce formal obligations with parties, terms, deadlines, cancellation/default rules and provenance.

## Communication channels

A message records sender, intended/actual recipient, payload propositions, channel, sent/due/delivered times, cost, custody, reliability and acquisition state. Channels include face-to-face, messenger, letter, newspaper and later telegraph, telephone, radio and digital infrastructure. Their availability and performance derive from technology and actual networks.

Communication failure, delay, interception or misunderstanding is a separate simulation process from initial intent parsing. Never punish a player for a parser bug by calling it an in-world misunderstanding. Actors react when they acquire the message, not when the player presses send.

## Reputation propagation

Record achievements or allegations with origin, witnesses, medium, location reach and credibility. A solved case can create a local reputation event; travelers or media deliver reports elsewhere. Reputation is not an instantaneous global scalar. Repeated retelling cannot create independent corroboration automatically: preserve source ancestry.

New opportunities arise from actual needs and known capabilities. A town seeking an investigator checks that it has received relevant information and can contact/hire the character. It must not know the player's class label or secret future success probability.

## Institutions and group behavior

Organizations act through authorized roles and budgets. Individual beliefs and institutional records are distinct. A clerk learning a fact does not necessarily inform every member instantly. Policies can instruct NPCs within constraints; members still use shared planning/resources and can encounter conflict or failure.

## Persistence, performance and acceptance

Persist commitments, message queues, relationship changes, source provenance and active plans. Aggregate anonymous routine behavior only when it preserves named actors and obligations. SC-NPC tests refusal, bounded planning and shared rules. SC-COMMUNICATION tests delayed delivery, rumor ancestry, interruption and remote authority. SC-GROUNDING checks that wording cannot create new commitments or knowledge.
