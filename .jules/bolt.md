## 2025-02-18 - Avoid eager evaluation on thread list components
**Learning:** Eagerly evaluating `is_alive()` via list comprehensions for thread states causes major overhead.
**Action:** Always prefer lazy evaluation with generator expressions, and ensure docstrings/parameters reflect iterable acceptance.
