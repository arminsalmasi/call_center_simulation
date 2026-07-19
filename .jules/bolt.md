## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2026-05-17 - Optimize dictionary lookups in hot loops
**Learning:** In this codebase's statistical aggregators (like `CallStatistics`), using the LBYL pattern (`if key not in dict`) introduces significant overhead during rapid evaluation in tight loops, especially when gathering per-call statistics.
**Action:** Replace LBYL checks with the EAFP pattern (`try...except KeyError`) and map the nested dictionary structure to a local variable to heavily reduce dictionary operations in hot loops.
