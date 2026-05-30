## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2026-05-30 - Eager Evaluation overhead in thread checking
**Learning:** In this codebase, eagerly evaluating `is_alive()` on lists of thread-based objects (like employees/freshers) introduces significant overhead.
**Action:** Prefer lazy evaluation or short-circuiting loops (like generators with `all()`) to minimize unnecessary thread state checks.
