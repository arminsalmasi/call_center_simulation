## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2026-06-16 - Optimize hot loop dictionary updates
**Learning:** In this codebase's statistical aggregators (e.g., `CallStatistics`), eagerly evaluating dictionaries using LBYL (`if key not in dict`) introduces significant execution overhead in tight loops.
**Action:** Always pre-allocate dictionaries when the size is known at initialization. In hot loops, prefer the EAFP pattern (`try...except KeyError`) and assign nested dictionary structures to a local variable to reduce multiple dictionary lookups and significantly reduce overhead.
