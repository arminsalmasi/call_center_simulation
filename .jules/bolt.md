## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2024-05-24 - Eager Thread State Evaluation Overhead
**Learning:** Eagerly evaluating `is_alive()` on large lists of thread objects (e.g., using list comprehensions like `[not f.is_alive() for f in freshers]`) introduces significant performance overhead and blocks short-circuiting logic in functions like `find_free_fresher_index`.
**Action:** Always prefer lazy evaluation (generator expressions like `all(not f.is_alive() for f in freshers)`) or passing the raw objects to rely on short-circuited iteration to minimize unnecessary thread state lock acquisitions.
