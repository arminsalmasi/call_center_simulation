## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.

## 2024-06-21 - Optimize statistical dictionary aggregation
**Learning:** In statistical aggregators like `CallStatistics`, evaluating dictionaries with LBYL (`if key not in dict`) adds substantial execution overhead inside hot loops.
**Action:** Pre-allocate dictionaries when limits are known (e.g. max freshers), use the EAFP pattern (`try...except KeyError`), and assign nested dictionaries to local variables for updates. This reduces overhead by bypassing bounds checking on every iteration.
