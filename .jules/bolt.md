## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.

## 2026-06-19 - Eager Thread State Evaluation Overhead
**Learning:** Eagerly evaluating `is_alive()` on lists of thread-based objects using list comprehensions (e.g., `[not f.is_alive() for f in freshers]`) introduces significant overhead and can crash iterators expecting actual thread objects.
**Action:** Prefer lazy evaluation and short-circuiting loops, like generator expressions or direct object passing, to minimize unnecessary state checks and type errors when passing to custom search functions.
