## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.

## 2024-05-18 - Eager evaluation of thread status causes major overhead
**Learning:** Eagerly evaluating `is_alive()` on a large list of threads (e.g., via `[not thread.is_alive() for thread in threads]`) adds significant processing overhead in rapid iteration loops, defeating short-circuit optimizations in downstream functions.
**Action:** Use raw lists and let functions short-circuit internally, or use generator expressions (e.g., `all(not thread.is_alive() for thread in threads)`) to lazily evaluate thread status and stop at the first condition match.
