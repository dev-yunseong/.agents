# agents/docs/performance.md

## Performance Rules

Optimize only when:
- there is measurable impact
- scaling is relevant
- profiling indicates bottlenecks

Avoid:
- premature optimization
- unreadable micro-optimizations
- complexity without evidence

---

## Preferred Optimizations

Prefer:
- reducing unnecessary allocations
- batching operations
- lazy evaluation
- async/non-blocking flow
- minimizing lock contention
- caching with explicit invalidation
- reducing redundant computation

---

## Backend

Prefer:
- streaming when appropriate
- efficient query design
- minimizing blocking IO
- connection reuse
- bounded concurrency

Avoid:
- N+1 queries
- unnecessary synchronization
- oversized transactions
- hidden global state

---

## Architecture

Performance should NOT:
- destroy readability
- increase coupling
- reduce maintainability
- introduce hidden behavior

Prefer:
- simple architecture first
- targeted optimization second

---

## Validation

Before optimization:
- identify the bottleneck
- explain expected gain
- explain tradeoffs

After optimization:
- validate actual improvement
- verify maintainability impact
