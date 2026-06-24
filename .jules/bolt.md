## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2024-06-11 - Use EAFP and local assignment for dictionary lookups in hot loops
**Learning:** Checking dictionary keys via LBYL (`if key not in dict`) and accessing nested dictionary elements directly multiple times adds significant execution overhead in tight hot loops.
**Action:** Use the EAFP pattern (`try...except KeyError`) for default assignment, and assign complex or nested elements to local variables when modifying them, which significantly reduces dict lookup overhead and execution time in Python.
