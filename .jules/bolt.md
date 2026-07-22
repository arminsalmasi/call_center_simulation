## 2024-03-24 - Eager Thread Evaluation Bottleneck
**Learning:** In this codebase, eagerly evaluating `is_alive()` using list comprehensions on large numbers of thread-based objects (like freshers) introduces massive overhead because thread state queries are expensive and unnecessary for the whole list once an available thread is found.
**Action:** Always prefer generator expressions (lazy evaluation) or short-circuiting loops when searching through thread-based objects to minimize unnecessary state checks.
## 2024-07-22 - Fast-path check in hot loops (Agent.try_assign)
**Learning:** Frequent lock acquisitions on thread-safe models (like Agent in call_center/models.py) create massive overhead during high load/hot loops, especially since agents are often already busy.
**Action:** Always check a busy flag before acquiring locks on highly contested models (Double-checked locking pattern).
