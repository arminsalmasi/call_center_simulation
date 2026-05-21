## 2024-05-18 - Avoid eager evaluation of Thread state
**Learning:** In this codebase, eagerly evaluating `is_alive()` on lists of thread-based objects (like employees/freshers) inside list comprehensions introduces unnecessary overhead and blocks the main execution flow if many threads are actively handled.
**Action:** Always prefer lazy evaluation (generator expressions) and short-circuiting when iterating over thread states or similar expensive method calls on multiple objects.
