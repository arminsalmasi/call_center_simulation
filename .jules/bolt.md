## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.

## 2026-05-18 - Dictionary lookup overhead in hot loops
**Learning:** In highly repetitive simulation processes, repeated LBYL (Look Before You Leap) dictionary lookup patterns (e.g., checking `if key not in dict` then accessing `dict[key]` twice for updates) introduce significant execution overhead.
**Action:** Pre-allocate dictionaries when possible, use the EAFP (Easier to Ask for Forgiveness than Permission) pattern with `try...except KeyError`, and assign the nested structure to a local variable to minimize redundant lookups.
