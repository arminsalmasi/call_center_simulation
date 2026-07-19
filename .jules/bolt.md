## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2026-05-24 - Lazy evaluation for thread states
**Learning:** Eagerly evaluating `is_alive()` on lists of thread-based objects via list comprehensions introduces significant overhead and unnecessary state checks compared to using lazy evaluation (generator expressions).
**Action:** Prefer generator expressions (e.g., `(t.is_alive() for t in threads)`) over list comprehensions (e.g., `[t.is_alive() for t in threads]`) to allow short-circuiting in operations like `all()`, `any()`, or custom iterator consumptions.
