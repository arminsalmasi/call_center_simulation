## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2026-05-17 - Fast Dictionary Lookups in Hot Loops
**Learning:** Checking for key existence `if key not in dict` before updating dictionary entries performs two lookups. In hot loops called millions of times in statistical simulations (e.g. `add_fresher_call`), this causes measurable overhead.
**Action:** Use the EAFP (Easier to Ask for Forgiveness than Permission) pattern with `try...except KeyError` block for dictionary updates, which reduces lookup overhead and shaves off significant execution time in high-frequency statistical aggregators.
