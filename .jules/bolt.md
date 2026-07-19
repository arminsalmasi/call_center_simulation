## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2023-10-27 - EAFP and Local Variables for Dict Access in Hot Loops
**Learning:** In statistical aggregators like `CallStatistics`, nested dictionary lookups using LBYL (`if key not in dict`) inside hot loops introduce significant execution overhead.
**Action:** Use the EAFP pattern (`try...except KeyError`) and assign nested dictionaries to local variables to substantially reduce execution time and dict lookup overhead.
