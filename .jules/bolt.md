## 2024-06-25 - Avoid Eager is_alive Checks on Thread Lists
**Learning:** Eagerly evaluating `is_alive()` on lists of thread-based objects (like freshers) inside list comprehensions introduces significant overhead, especially for long lists or when called frequently.
**Action:** Always prefer lazy evaluation (generator expressions) and short-circuiting logic when checking the state of multiple threads (e.g., using `any()` or `all()`) to minimize unnecessary thread state checks.
