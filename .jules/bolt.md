## 2024-03-24 - Eager Thread Evaluation Bottleneck
**Learning:** In this codebase, eagerly evaluating `is_alive()` using list comprehensions on large numbers of thread-based objects (like freshers) introduces massive overhead because thread state queries are expensive and unnecessary for the whole list once an available thread is found.
**Action:** Always prefer generator expressions (lazy evaluation) or short-circuiting loops when searching through thread-based objects to minimize unnecessary state checks.

## 2024-07-20 - Thread Contention Overhead in Hot Loops
**Learning:** In this codebase, frequent lock acquisitions on busy thread-safe models (e.g., checking `self._state` inside a lock in `Agent.try_assign` in `call_center/models.py`) create severe performance bottlenecks in hot loops.
**Action:** Applying a double-checked locking pattern (a lock-free fast-path state check before acquiring the lock) significantly reduces thread contention overhead.
