## 2026-05-17 - Avoid cryptographic rng for general simulations
**Learning:** The codebase was using `secrets.SystemRandom().randint()` for generating call metrics (duration, waves, intervals) which is a cryptographic operation reading from system entropy (`/dev/urandom`). This adds massive overhead to rapid generation in large-scale simulation threads compared to a pseudo-random number generator.
**Action:** Use standard `random.randint()` for statistical/simulation randomization tasks where cryptographic security is not required, resulting in up to 5-6x speedup in standalone number generation overhead.
## 2024-06-08 - Optimize Dictionary Lookups in Hot Loops using EAFP
**Learning:** Eager lookups (`if key not in dict`) combined with multiple sequential nested dictionary assignments (e.g., `dict[key]['count'] += 1`) introduce significant overhead in this codebase's hot simulation paths like `CallStatistics`.
**Action:** Use the EAFP pattern (`try...except KeyError`) and map the nested dictionary value to a local variable (`stats = self.fresher_statistics[index]`) before performing operations, reducing multiple hash lookups to just one on the hot path.
