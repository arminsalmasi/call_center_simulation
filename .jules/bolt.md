## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2024-05-23 - Generator Expressions for Short-Circuiting
**Learning:** Using `all([not condition for item in list])` evaluates the entire list comprehension before passing it to `all()`, which builds an unnecessary list in memory and prevents short-circuiting.
**Action:** Replace with `not any(condition for item in list)` to fully utilize short-circuiting and prevent unnecessary list memory allocation.
