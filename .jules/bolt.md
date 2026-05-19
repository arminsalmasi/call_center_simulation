## 2024-05-19 - Optimize `is_alive()` Evaluation on Threads
**Learning:** Eagerly evaluating `is_alive()` on lists of thread-based objects (like employees/freshers) introduces significant threading overhead.
**Action:** Prefer lazy evaluation (like generator expressions) or short-circuiting loops to minimize unnecessary thread state checks.
