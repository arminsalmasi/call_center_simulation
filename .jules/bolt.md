## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2024-05-24 - Avoid eager list comprehensions for thread state evaluation
**Learning:** Evaluating thread status using list comprehensions inside short-circuiting functions like `all()` creates a full list in memory on every call, sacrificing performance and short-circuiting capabilities.
**Action:** Use generator expressions inside `all()` and `any()` (e.g., `all(not f.is_alive() for f in freshers)`) to avoid memory overhead and leverage lazy evaluation.
