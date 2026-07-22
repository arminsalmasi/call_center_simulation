"""Agent models with idle/busy state machine."""

from __future__ import annotations

import random
import threading
import time
from enum import Enum
from typing import Callable


class Role(str, Enum):
    FRESHER = "fresher"
    TECHNICAL_LEAD = "technical_lead"
    PROJECT_MANAGER = "project_manager"


class AgentState(str, Enum):
    IDLE = "idle"
    BUSY = "busy"


class Agent:
    """Stable agent identity; each call runs on a fresh worker thread."""

    def __init__(
        self,
        name: str,
        role: Role,
        index: int | None = None,
        duration_range: tuple[int, int] = (1, 1),
        rng: random.Random | None = None,
        on_event: Callable[..., None] | None = None,
        sleep_fn: Callable[[float], None] = time.sleep,
    ) -> None:
        self.name = name
        self.role = role
        self.index = index
        self.duration_range = duration_range
        self._rng = rng or random.Random()
        self._on_event = on_event
        self._sleep = sleep_fn
        self._lock = threading.Lock()
        self._condition = threading.Condition(self._lock)
        self._state = AgentState.IDLE
        self._current_duration = 0
        self._active_thread: threading.Thread | None = None
        self.calls_handled = 0

    @property
    def state(self) -> AgentState:
        with self._lock:
            return self._state

    def is_idle(self) -> bool:
        with self._lock:
            return self._state is AgentState.IDLE

    def snapshot(self) -> dict:
        with self._lock:
            return {
                "name": self.name,
                "role": self.role.value,
                "index": self.index,
                "state": self._state.value,
                "current_duration": self._current_duration,
                "calls_handled": self.calls_handled,
            }

    def try_assign(self) -> int | None:
        """Assign a call if idle. Returns duration, or None if busy."""
        # Fast-path check without lock to reduce thread contention
        if self._state is not AgentState.IDLE:
            return None
        with self._condition:
            if self._state is not AgentState.IDLE:
                return None
            duration = self._rng.randint(self.duration_range[0], self.duration_range[1])
            self._state = AgentState.BUSY
            self._current_duration = duration
            self.calls_handled += 1
            thread = threading.Thread(
                target=self._handle_call,
                args=(duration,),
                name=f"{self.name}-call",
                daemon=True,
            )
            self._active_thread = thread
            thread.start()
        if self._on_event:
            self._on_event(
                "call_assigned",
                f"{self.name} took a call ({duration}s)",
                agent=self.name,
                role=self.role.value,
                index=self.index,
                duration=duration,
            )
        return duration

    def _handle_call(self, duration: int) -> None:
        try:
            self._sleep(duration)
        finally:
            with self._condition:
                self._state = AgentState.IDLE
                self._current_duration = 0
                self._active_thread = None
                self._condition.notify_all()
            if self._on_event:
                self._on_event(
                    "call_finished",
                    f"{self.name} hung up",
                    agent=self.name,
                    role=self.role.value,
                    index=self.index,
                    duration=duration,
                )

    def wait_until_idle(self, timeout: float | None = None) -> bool:
        with self._condition:
            if self._state is AgentState.IDLE:
                return True
            return self._condition.wait(timeout=timeout)
