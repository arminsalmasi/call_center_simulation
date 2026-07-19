## 2024-05-24 - Lazy evaluation for search functions
**Learning:** Using a list comprehension `[condition(x) for x in xs]` inside a search function like `find_free_fresher_index` forces Python to evaluate the condition for *all* elements before the search even begins. This wastes CPU and memory if the search function can return early.
**Action:** Replace list comprehensions with generator expressions `(condition(x) for x in xs)` when passing them to functions that can short-circuit or return early. This allows lazy evaluation and significant speedups in tight loops.
