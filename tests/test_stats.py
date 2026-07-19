"""Unit tests for call statistics."""

from concurrent.futures import ThreadPoolExecutor

from call_center.stats import CallStatistics


def test_add_fresher_call_preallocated():
    stats = CallStatistics(2)
    stats.add_fresher_call(0, 5)
    stats.add_fresher_call(0, 3)
    snap = stats.snapshot()
    assert snap["freshers"]["0"] == {"counter": 2, "call_duration": 8}


def test_add_fresher_call_dynamic():
    stats = CallStatistics(0)
    stats.add_fresher_call(7, 4)
    assert stats.snapshot()["freshers"]["7"]["counter"] == 1


def test_lead_and_manager_and_busy():
    stats = CallStatistics()
    stats.add_technical_lead_call(2)
    stats.add_project_manager_call(3)
    stats.add_busy_drop()
    snap = stats.snapshot()
    assert snap["technical_lead"]["counter"] == 1
    assert snap["project_manager"]["call_duration"] == 3
    assert snap["busy_drops"] == 1


def test_stats_thread_safety_smoke():
    stats = CallStatistics(4)

    def worker(i: int) -> None:
        for _ in range(50):
            stats.add_fresher_call(i % 4, 1)

    with ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(worker, range(8)))

    snap = stats.snapshot()
    total = sum(v["counter"] for v in snap["freshers"].values())
    assert total == 400
