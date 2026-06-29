## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2024-06-29 - Generator expressions inside any/all are faster than list comprehensions inside all
**Learning:** In hot loops checking thread states in Python (e.g. `all([not f.is_alive() for f in freshers]`), evaluating all states into a list and passing to `all()` defeats short-circuiting and consumes memory.
**Action:** Use generator expressions like `not any(f.is_alive() for f in freshers)` which short-circuits instantly and avoids allocating list memory overhead.
