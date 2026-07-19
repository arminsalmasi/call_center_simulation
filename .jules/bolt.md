## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.

## 2026-05-18 - EAFP Pattern for Dictionary Operations
**Learning:** In this codebase's statistical aggregators (e.g., `CallStatistics`), checking dictionary keys before updating (LBYL) introduces significant overhead during simulation. Pre-allocating the dictionary with dictionary comprehensions when possible, and utilizing the EAFP pattern (`try...except KeyError`) instead of LBYL, significantly reduces execution overhead.
**Action:** Use dictionary comprehensions to pre-allocate memory and use the EAFP pattern (`try...except KeyError`) instead of `if key not in dict` in hot loops.
