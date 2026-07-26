## 2026-07-26 - [Avoid O(N log N) overhead in snapshot]
**Learning:** In CallStatistics, since `fresher_statistics` is pre-allocated sequentially in `__init__`, Python 3.7+ guarantees insertion order, which means it is already sorted by ID. Sorting it again in hot loops like `snapshot` causes unnecessary overhead and increases lock contention duration.
**Action:** When a dictionary is sequentially pre-allocated, rely on Python's insertion-order guarantee rather than explicitly calling `sorted()`.
