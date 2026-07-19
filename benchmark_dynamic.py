import time
from call_center_simulation import CallStatistics

def measure_preallocated():
    start = time.perf_counter()
    stats = CallStatistics(1000)
    for _ in range(1000):
        for i in range(1000):
            stats.add_fresher_call(i, 10)
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    t = measure_preallocated()
    print(f"Improved Time: {t:.4f} seconds")
