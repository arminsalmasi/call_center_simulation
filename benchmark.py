import timeit

setup = """
class MockFresher:
    def __init__(self, is_alive_val):
        self._is_alive = is_alive_val
    def is_alive(self):
        return self._is_alive

# Create a list of 100 freshers, all busy except the last one
freshers = [MockFresher(True) for _ in range(99)] + [MockFresher(False)]

def find_free_fresher_index(bool_list):
    for index, value in enumerate(bool_list):
        if value:
            return index
    return -1
"""

old_code = """
idx = find_free_fresher_index([not fresher.is_alive() for fresher in freshers])
"""

new_code = """
idx = next((i for i, fresher in enumerate(freshers) if not fresher.is_alive()), -1)
"""

old_time = timeit.timeit(old_code, setup=setup, number=10000)
new_time = timeit.timeit(new_code, setup=setup, number=10000)

print(f"Old time: {old_time:.5f} seconds")
print(f"New time: {new_time:.5f} seconds")
print(f"Improvement: {(old_time - new_time) / old_time * 100:.2f}%")
