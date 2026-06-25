## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2024-06-25 - Pre-allocate dicts and EAFP in CallStatistics
**Learning:** In this codebase's statistical aggregators (e.g., `CallStatistics`), pre-allocating dictionaries and using the EAFP pattern (`try...except KeyError`) with local variable assignments in hot loops significantly reduces execution overhead compared to LBYL (`if key not in dict`).
**Action:** Always pre-allocate dictionary keys if bounds are known, and assign nested structures to local variable inside a `try/except` block to handle hot-loop metrics collection.
