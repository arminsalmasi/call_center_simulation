## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.

## 2026-05-18 - EAFP over LBYL in inner simulation loops
**Learning:** Checking for dict key existence with `if key not in dict` (LBYL) before mutating inner structures causes a significant double-lookup penalty inside deep simulation loops, bottlenecking thread statistics aggregation.
**Action:** Use the EAFP pattern (`try...except KeyError`) and map inner dicts to local variables to eliminate redundant hash lookups when aggregating hot path statistics.
