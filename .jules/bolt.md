## 2024-03-24 - Eager Thread Evaluation Bottleneck
**Learning:** In this codebase, eagerly evaluating `is_alive()` using list comprehensions on large numbers of thread-based objects (like freshers) introduces massive overhead because thread state queries are expensive and unnecessary for the whole list once an available thread is found.
**Action:** Always prefer generator expressions (lazy evaluation) or short-circuiting loops when searching through thread-based objects to minimize unnecessary state checks.
## 2024-05-24 - Double-Checked Locking in Agent.try_assign
**Learning:** In this codebase, frequent lock acquisitions on busy thread-safe models (e.g., checking `self._state` inside a lock in `Agent.try_assign` in `call_center/models.py`) create severe performance bottlenecks in hot loops.
**Action:** Applying a double-checked locking pattern (a lock-free fast-path state check before acquiring the lock) significantly reduces thread contention overhead.
## 2024-05-24 - EventBus O(N) History Bottleneck
**Learning:** In this codebase, maintaining a fixed-size event history in `EventBus` (`call_center/events.py`) using list slicing (`_history[-limit:]`) creates an O(N) performance bottleneck.
**Action:** Using `collections.deque(maxlen=limit)` resolves this by providing O(1) appends.
## 2024-05-24 - dataclasses.asdict Bottleneck
**Learning:** Using `dataclasses.asdict` inside tight serialization loops (e.g. `SimulationEvent.to_dict()` called thousands of times) introduces severe overhead because it recursively copies elements using deepcopy-like behavior.
**Action:** Replace `asdict` with a manual dictionary construction in the hot path. This can reduce serialization execution time from ~0.50s to ~0.03s per 100k iterations.
