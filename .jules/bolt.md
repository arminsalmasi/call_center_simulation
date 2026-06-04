## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2024-06-04 - Avoid eager thread state evaluation
**Learning:** Eagerly evaluating `is_alive()` on lists of thread-based objects using list comprehensions (e.g. `all([not thread.is_alive() for thread in threads])`) defeats short-circuiting capabilities and introduces significant overhead due to unnecessary thread state checks.
**Action:** When checking state across multiple threads, always prefer lazy evaluation with generator expressions (e.g., `not any(thread.is_alive() for thread in threads)`) to allow early exit and minimize lock contention/overhead.
