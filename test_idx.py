class MockFresher:
    def is_alive(self):
        return False

def find_free_fresher_index(freshers):
    for index, fresher in enumerate(freshers):
        if not fresher.is_alive():
            return index
    return -1

freshers = [MockFresher()]
try:
    find_free_fresher_index([not fresher.is_alive() for fresher in freshers])
except Exception as e:
    print(f"Original crashed: {e}")

try:
    print(f"Fixed result: {find_free_fresher_index(freshers)}")
except Exception as e:
    print(f"Fixed crashed: {e}")
