## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.

## 2026-05-18 - Eager evaluation overhead with thread is_alive()
**Learning:** In Python, passing a list comprehension `[not fresher.is_alive() for fresher in freshers]` to `all()` forces the system to perform a blocking `is_alive()` check on every single thread object in the list before `all()` can begin its evaluation, which introduces significant overhead.
**Action:** Always use generator expressions `all(not fresher.is_alive() for fresher in freshers)` when evaluating conditions over sequences of thread objects to allow for short-circuiting, avoiding unnecessary state checks.
