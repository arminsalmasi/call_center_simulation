## 2024-05-18 - Avoid Eager Evaluation of Thread States in Lists
**Learning:** Eagerly evaluating `is_alive()` on a list of Thread objects (like the `Fresher` list) via list comprehension forces all thread states to be queried unnecessarily.
**Action:** Use short-circuiting logic (e.g., iterating directly and returning on the first hit) instead of passing eagerly evaluated boolean lists to functions.
