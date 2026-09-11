# Economy, logistics, trade and property

Version 0.2 | Owner: economy-systems lead | Requirement PR-011

## State and authority

Economy owns production/consumption plans, markets, prices, orders, wages, payments and obligations. Property owns title, custody, access, liens and transfers. Logistics owns shipments, routes, capacity, departure/arrival schedules and custody transitions. Inventories remain authoritative entity quantities shared through transactions, not separate duplicated shop totals.

Money uses integer minor units plus currency ID. Goods use typed quantities and quality/provenance. All transfers name source and destination; production/destruction name their explicit sources/sinks. Monetary issuance, taxes, fees, wages and credit cannot be unexplained balance changes. A financial ledger is a game-system model, not a real-world accounting service.

## Trade and price discovery

Markets observe actual stock, committed demand, local availability and recent trades. Price updates use bounded, smoothed functions with minimum denominators, rate limits and versioned parameters to avoid unstable runaway feedback. Supply, transport costs, quality, relationships and bargaining can influence quotes. The initial implementation favors understandable local markets over a universal perfect-information exchange.

A quote has seller, buyer, items/quantities, currency, unit/total amounts, validity window and relevant inventory revision. Accepting a stale quote revalidates or returns a new preview; it never silently raises authorized spending. Barter transfers both sides atomically. NPC refusal/counteroffer is a social decision before asset transfer.

## Production and labor

A production order references a validated process, owned/reserved materials, tools, facility, labor, duration and expected outputs/waste. Partial work is persistent. Workers cannot simultaneously provide full labor to incompatible jobs. Employment agreements specify pay, schedule, permissions and termination/default rules. Wages require actual funds or an explicit payable obligation.

## Logistics

Shipments contain unique cargo claims, custody, route segments, capacity, departure/arrival estimates and interruption policy. Route changes can delay, reroute or cancel delivery. Goods in transit are not also available in a shop. Loss/damage updates cargo and contractual consequences in the same causal chain.

Distributed regional processing uses a persisted transfer ledger to reconcile exactly once. A region unload or reload cannot duplicate a shipment or deliver it early. Distant markets do not immediately know another town's stock or price without a channel.

## Ownership and contracts

Ownership, possession and permission differ. Borrowed equipment remains owned by its lender. Taking another person's property creates an attempted action and possible crime, not an automatically legitimate transfer. Inheritance, sale, liens, institutional title and abandonment use explicit rule versions and events.

Contracts record parties, consideration, delivery/service obligations, deadlines, authority, enforcement venue and resolution. The simulation commits terms before generated dialogue describes them. A model cannot invent a loan, forgive a debt or change a budget.

## Balancing and analytics

Track stockouts, production bottlenecks, trade volume, wealth distribution, employment, defaults and household sufficiency by seed. Prevent accidental infinite-money cycles through conservation/transaction tests, not hidden corrective money creation. Intentional market interventions require explicit institutional sources and events.

## Acceptance

SC-ECONOMY covers barter atomicity, price expiry, money/quantity conservation, failed payment, credit obligations and ownership. SC-LOGISTICS covers capacity, route disruption, in-transit uniqueness and cross-region delivery. SC-REGIONAL proves that shortages arise from actual logistics and can produce employment, construction or trade opportunities.
