"""Router escalation tests."""

import threading

from call_center.models import Agent, Role
from call_center.router import RouteResult, Router
from call_center.stats import CallStatistics


def _blocking_agent(name: str, role: Role, index: int | None = None) -> tuple[Agent, threading.Event]:
    release = threading.Event()

    def sleep_fn(_seconds: float) -> None:
        release.wait(timeout=5)

    agent = Agent(
        name=name,
        role=role,
        index=index,
        duration_range=(1, 1),
        sleep_fn=sleep_fn,
    )
    return agent, release


def test_routes_to_first_idle_fresher():
    stats = CallStatistics(2)
    f1, release1 = _blocking_agent("f1", Role.FRESHER, 0)
    f2, _ = _blocking_agent("f2", Role.FRESHER, 1)
    tl, _ = _blocking_agent("tl", Role.TECHNICAL_LEAD)
    pm, _ = _blocking_agent("pm", Role.PROJECT_MANAGER)
    router = Router([f1, f2], tl, pm, stats)

    outcome = router.route_call()
    assert outcome.result is RouteResult.FRESHER
    assert outcome.fresher_index == 0
    assert stats.snapshot()["freshers"]["0"]["counter"] == 1
    release1.set()


def test_escalates_to_technical_lead():
    stats = CallStatistics(1)
    fresher, release_f = _blocking_agent("f1", Role.FRESHER, 0)
    assert fresher.try_assign() is not None
    tl, release_tl = _blocking_agent("tl", Role.TECHNICAL_LEAD)
    pm, _ = _blocking_agent("pm", Role.PROJECT_MANAGER)
    router = Router([fresher], tl, pm, stats)

    outcome = router.route_call()
    assert outcome.result is RouteResult.TECHNICAL_LEAD
    assert stats.snapshot()["technical_lead"]["counter"] == 1
    release_f.set()
    release_tl.set()


def test_escalates_to_project_manager_then_busy():
    stats = CallStatistics(0)
    tl, release_tl = _blocking_agent("tl", Role.TECHNICAL_LEAD)
    pm, release_pm = _blocking_agent("pm", Role.PROJECT_MANAGER)
    assert tl.try_assign() is not None
    router = Router([], tl, pm, stats)

    first = router.route_call()
    assert first.result is RouteResult.PROJECT_MANAGER

    second = router.route_call()
    assert second.result is RouteResult.BUSY
    assert stats.snapshot()["busy_drops"] == 1
    release_tl.set()
    release_pm.set()
