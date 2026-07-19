## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.

## 2024-05-24 - EAFP for dictionary hot loops
**Learning:** Using the LBYL pattern (`if key not in dict`) for dictionary aggregation in hot loops is slower than the EAFP pattern (`try...except KeyError`) combined with local variable assignment.
**Action:** Use the EAFP pattern and local variable assignment for nested dictionary operations in statistical aggregators (e.g. `CallStatistics`) to significantly reduce execution overhead.
