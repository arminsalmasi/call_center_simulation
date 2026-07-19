"""Call center simulation engine."""

from __future__ import annotations

import logging
import random
import threading
import time
from dataclasses import dataclass
from typing import Any, Callable

from call_center.events import EventBus
from call_center.models import Agent, Role
from call_center.router import RouteResult, Router
from call_center.stats import CallStatistics
from call_center.validation import validate_simulation_params

logger = logging.getLogger(__name__)


@dataclass
class SimulationConfig:
    number_of_freshers: int
    run_time: float
    min_max_calls_per_wave: tuple[int, int]
    min_max_sleep_interval: tuple[int, int]
    min_max_call_duration: tuple[int, int]
    seed: int | None = None

    @classmethod
    def create(
        cls,
        number_of_freshers: object,
        run_time: object,
        min_max_calls_per_wave: tuple[object, object],
        min_max_sleep_interval: tuple[object, object],
        min_max_call_duration: tuple[object, object],
        seed: int | None = None,
    ) -> SimulationConfig:
        n, rt, calls, sleep, duration = validate_simulation_params(
            number_of_freshers,
            run_time,
            min_max_calls_per_wave,
            min_max_sleep_interval,
            min_max_call_duration,
        )
        return cls(
            number_of_freshers=n,
            run_time=rt,
            min_max_calls_per_wave=calls,
            min_max_sleep_interval=sleep,
            min_max_call_duration=duration,
            seed=seed,
        )


class CallCenterSimulation:
    """Orchestrates wave scheduling, routing, and agent lifecycle."""

    def __init__(
        self,
        config: SimulationConfig | None = None,
        event_bus: EventBus | None = None,
        sleep_fn: Callable[[float], None] = time.sleep,
        number_of_freshers: int = 0,
    ) -> None:
        self.config = config
        self.event_bus = event_bus or EventBus()
        self._sleep = sleep_fn
        self._lock = threading.RLock()
        self._stop = threading.Event()
        self._done = threading.Event()
        self._runner: threading.Thread | None = None
        self._status = "idle"
        self.stats = CallStatistics(number_of_freshers)
        self.freshers: list[Agent] = []
        self.technical_lead: Agent | None = None
        self.project_manager: Agent | None = None
        self._rng = random.Random()
        self.loop_number = 0
        self.busy_messages = 0

    def set(
        self,
        number_of_freshers: object,
        run_time: object,
        min_max_calls_per_wave: tuple[object, object],
        min_max_sleep_interval: tuple[object, object],
        min_max_call_duration: tuple[object, object],
        seed: int | None = None,
    ) -> None:
        self.config = SimulationConfig.create(
            number_of_freshers,
            run_time,
            min_max_calls_per_wave,
            min_max_sleep_interval,
            min_max_call_duration,
            seed=seed,
        )

    def _emit(self, kind: str, message: str, **payload: Any) -> None:
        self.event_bus.emit(kind, message, **payload)

    def _build_agents(self) -> None:
        assert self.config is not None
        cfg = self.config
        if cfg.seed is not None:
            self._rng.seed(cfg.seed)
        self.stats = CallStatistics(cfg.number_of_freshers)

        def on_event(kind: str, message: str, **payload: Any) -> None:
            self._emit(kind, message, **payload)

        self.freshers = [
            Agent(
                name=f"fresher {i + 1}",
                role=Role.FRESHER,
                index=i,
                duration_range=cfg.min_max_call_duration,
                rng=random.Random(self._rng.random()),
                on_event=on_event,
                sleep_fn=self._sleep,
            )
            for i in range(cfg.number_of_freshers)
        ]
        self.technical_lead = Agent(
            name="technical lead",
            role=Role.TECHNICAL_LEAD,
            duration_range=cfg.min_max_call_duration,
            rng=random.Random(self._rng.random()),
            on_event=on_event,
            sleep_fn=self._sleep,
        )
        self.project_manager = Agent(
            name="project manager",
            role=Role.PROJECT_MANAGER,
            duration_range=cfg.min_max_call_duration,
            rng=random.Random(self._rng.random()),
            on_event=on_event,
            sleep_fn=self._sleep,
        )

    def _process_wave(self, router: Router, loop_number: int) -> None:
        assert self.config is not None
        number_of_calls = self._rng.randint(*self.config.min_max_calls_per_wave)
        self._emit(
            "wave",
            f"Incoming calls: {number_of_calls}, loop: {loop_number}",
            calls=number_of_calls,
            loop=loop_number,
        )
        print(f"\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
        print(f"Incoming calls: {number_of_calls}, loop: {loop_number}")
        print("----------------------------------------------")

        for call_idx in range(number_of_calls):
            if self._stop.is_set():
                return
            print(f"Call {call_idx + 1} is on top of the queue.")
            print("----------------------")
            outcome = router.route_call()
            if outcome.result is RouteResult.BUSY:
                self.busy_messages += 1
                print("All lines are busy. Please try again later.")
                print("----------------------------------------------")
                self._emit("busy", "All lines are busy")
            elif outcome.agent is not None:
                print(
                    f"{outcome.agent.name} is free and will answer the call "
                    f"({outcome.duration}s)."
                )

    def _wait_for_idle(self, timeout: float = 60.0) -> None:
        agents = list(self.freshers)
        if self.technical_lead:
            agents.append(self.technical_lead)
        if self.project_manager:
            agents.append(self.project_manager)

        deadline = time.monotonic() + timeout
        for agent in agents:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                logger.warning("Timeout waiting for remaining calls to finish.")
                return
            agent.wait_until_idle(timeout=remaining)

    def run_simulation(self, *, background: bool = False) -> bool:
        if self.config is None:
            raise RuntimeError("Simulation config not set; call set() first")

        with self._lock:
            if self._status == "running":
                raise RuntimeError("Simulation already running")
            self._stop.clear()
            self._done.clear()
            self._status = "running"
            self.loop_number = 0
            self.busy_messages = 0
            # Fresh bus each run so prior SSE closers do not poison a new session.
            self.event_bus = EventBus()

        if background:
            self._runner = threading.Thread(
                target=self._run_body, name="simulation-runner", daemon=True
            )
            self._runner.start()
            return True

        return self._run_body()

    def _run_body(self) -> bool:
        try:
            self._build_agents()
            assert self.config is not None
            assert self.technical_lead is not None
            assert self.project_manager is not None

            router = Router(
                self.freshers, self.technical_lead, self.project_manager, self.stats
            )
            end_time = time.monotonic() + self.config.run_time
            self._emit("started", "Simulation started")

            loop_number = 1
            while not self._stop.is_set() and time.monotonic() < end_time:
                self.loop_number = loop_number
                self._process_wave(router, loop_number)
                if self._stop.is_set():
                    break
                interval = self._rng.randint(*self.config.min_max_sleep_interval)
                print(
                    f"Waiting for {interval} seconds before initiating the next wave of calls."
                )
                print("----------------------------------------------")
                self._emit("wait", f"Waiting {interval}s for next wave", seconds=interval)
                # Interruptible sleep
                remaining = interval
                while remaining > 0 and not self._stop.is_set():
                    step = min(0.25, remaining)
                    self._sleep(step)
                    remaining -= step
                loop_number += 1

            self._wait_for_idle(timeout=60.0)
            self.stats.print_summary()
            self._emit("finished", "Simulation finished", stats=self.stats.snapshot())
            with self._lock:
                self._status = "finished"
            return True
        except Exception as exc:
            logger.exception("Simulation failed")
            self._emit("error", str(exc))
            with self._lock:
                self._status = "error"
            raise
        finally:
            self._done.set()
            self.event_bus.close()

    def stop(self, wait: bool = True, timeout: float = 30.0) -> None:
        self._stop.set()
        self._emit("stopping", "Stop requested")
        if wait and self._runner is not None:
            self._runner.join(timeout=timeout)
        with self._lock:
            if self._status == "running":
                self._status = "stopped"

    def status_snapshot(self) -> dict[str, Any]:
        with self._lock:
            status = self._status
            loop = self.loop_number
            cfg = self.config
        agents = [a.snapshot() for a in self.freshers]
        if self.technical_lead:
            agents.append(self.technical_lead.snapshot())
        if self.project_manager:
            agents.append(self.project_manager.snapshot())
        return {
            "status": status,
            "loop": loop,
            "config": None
            if cfg is None
            else {
                "number_of_freshers": cfg.number_of_freshers,
                "run_time": cfg.run_time,
                "min_max_calls_per_wave": list(cfg.min_max_calls_per_wave),
                "min_max_sleep_interval": list(cfg.min_max_sleep_interval),
                "min_max_call_duration": list(cfg.min_max_call_duration),
                "seed": cfg.seed,
            },
            "agents": agents,
            "stats": self.stats.snapshot(),
            "busy_messages": self.busy_messages,
            "recent_events": self.event_bus.recent(30),
        }
