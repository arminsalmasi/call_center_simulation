import time
from call_center_simulation import CallStatistics

def benchmark():
    try:
        stats = CallStatistics(1000)
    except TypeError:
        stats = CallStatistics()

    start = time.perf_counter()
    for _ in range(5000):
        for i in range(1000):
            try:
                stats.add_fresher_call(i, 10)
            except IndexError:
                # Fallback if resizing is disabled but not pre-allocated
                pass
    end = time.perf_counter()
    print(f"Time taken: {end - start:.4f} seconds")

if __name__ == "__main__":
    benchmark()
