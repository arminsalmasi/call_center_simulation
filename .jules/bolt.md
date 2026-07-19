## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2024-05-17 - EAFP Pattern for Hot Loop Lookups
**Learning:** In statistical aggregation within large loop simulations, the "Look Before You Leap" (LBYL) dictionary access pattern introduces significant overhead due to multiple hash lookups per iteration.
**Action:** Always prefer the "Easier to Ask for Forgiveness than Permission" (EAFP) pattern (`try...except KeyError`) in hot-path dictionary operations when key hits are common. Assign nested dictionaries to local variables to further reduce lookups.
