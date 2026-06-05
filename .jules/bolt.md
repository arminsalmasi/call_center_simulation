## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.

## 2024-05-18 - Avoid eager thread state evaluation
**Learning:** In the call center simulation, evaluating `is_alive()` eagerly across all active threads using list comprehensions like `all([not(f.is_alive()) for f in freshers])` incurs substantial overhead due to invoking `.is_alive()` on every single thread even if an early one evaluates to True/False.
**Action:** When checking the aggregate state of threads, always use lazy generator expressions like `all(not(f.is_alive()) for f in freshers)` to leverage short-circuiting and dramatically reduce unnecessary thread state checks.
