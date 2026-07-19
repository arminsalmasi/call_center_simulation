## 2024-05-24 - Lazy evaluation of thread states
**Learning:** Eagerly evaluating `is_alive()` on a large list of threads (like employees/freshers in this architecture) introduces significant overhead.
**Action:** Use generator expressions for lazy evaluation or short-circuit loops to minimize unnecessary thread state checks.
