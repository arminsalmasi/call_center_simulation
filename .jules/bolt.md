## 2024-03-24 - Eager Thread Evaluation Bottleneck
**Learning:** In this codebase, eagerly evaluating `is_alive()` using list comprehensions on large numbers of thread-based objects (like freshers) introduces massive overhead because thread state queries are expensive and unnecessary for the whole list once an available thread is found.
**Action:** Always prefer generator expressions (lazy evaluation) or short-circuiting loops when searching through thread-based objects to minimize unnecessary state checks.
## 2024-05-18 - Lock Contention in Try-Assign Pattern
**Learning:** In highly concurrent environments where agents are frequently busy, unconditionally acquiring a thread lock just to check state (`self._state is not AgentState.IDLE`) creates massive lock contention overhead in hot loops.
**Action:** Use a double-checked locking pattern for simple optimistic reads: perform a lock-free fast-path state check first, and only acquire the lock if the state appears actionable (e.g., `IDLE`).
