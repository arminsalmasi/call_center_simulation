## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2024-05-15 - Optimizing Statistical Aggregators
**Learning:** In this codebase's statistical aggregators (e.g., CallStatistics), using Look-Before-You-Leap (if key not in dict) combined with multiple dictionary lookups in hot loops creates significant execution overhead.
**Action:** Use the EAFP pattern (try...except KeyError) and assign nested dictionaries to local variables to significantly reduce execution overhead in hot loops.
