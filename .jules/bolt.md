## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2024-05-18 - Optimize statistical aggregators with EAFP
**Learning:** In this codebase's statistical aggregators (e.g., `CallStatistics`), using the EAFP pattern (`try...except KeyError`) instead of LBYL (`if key not in dict`), and assigning nested dictionaries to local variables for operations in hot loops significantly reduces execution overhead.
**Action:** Always prefer EAFP (`try/except KeyError`) over LBYL (`if not in`) and cache nested dictionary lookups locally in performance-critical statistical aggregation methods.
