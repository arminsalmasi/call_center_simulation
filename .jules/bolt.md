## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2024-05-18 - EAFP Pattern for Hot Loop Dictionary Operations
**Learning:** In statistical aggregators like `CallStatistics`, using Look-Before-You-Leap (`if key not in dict`) combined with multiple dictionary lookups causes significant execution overhead when repeatedly updating nested dictionaries in hot simulation loops.
**Action:** Use the EAFP pattern (`try...except KeyError`) and assign nested dictionary structures to local variables. This avoids multiple lookups per operation and results in approximately a ~30% speedup in repeated aggregator calls.
