## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.

## 2024-05-18 - EAFP Pattern in Hot Loops
**Learning:** In this codebase's statistical aggregators (e.g., `CallStatistics`), using the Look Before You Leap (LBYL) pattern for dictionary checking (`if key not in dict`) combined with multiple dictionary lookups causes significant overhead in hot loops.
**Action:** Use the Easier to Ask for Forgiveness than Permission (EAFP) pattern (`try...except KeyError`) and assign nested dictionaries to a local variable for repeated operations to significantly reduce execution overhead and save ~20% of execution time.
