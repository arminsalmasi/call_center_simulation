"""Thread-safe call statistics."""

from __future__ import annotations

import threading
from typing import Any


class CallStatistics:
    def __init__(self, num_freshers: int = 0) -> None:
        self._lock = threading.Lock()
        self.fresher_statistics: dict[int, dict[str, int]] = {
            i: {"counter": 0, "call_duration": 0} for i in range(num_freshers)
        }
        self.technical_lead_counter = 0
        self.technical_lead_call_duration = 0
        self.project_manager_counter = 0
        self.project_manager_call_duration = 0
        self.busy_drops = 0

    def add_fresher_call(self, index: int, call_duration: int) -> None:
        with self._lock:
            try:
                stats = self.fresher_statistics[index]
                stats["counter"] += 1
                stats["call_duration"] += call_duration
            except KeyError:
                self.fresher_statistics[index] = {
                    "counter": 1,
                    "call_duration": call_duration,
                }

    def add_technical_lead_call(self, call_duration: int) -> None:
        with self._lock:
            self.technical_lead_counter += 1
            self.technical_lead_call_duration += call_duration

    def add_project_manager_call(self, call_duration: int) -> None:
        with self._lock:
            self.project_manager_counter += 1
            self.project_manager_call_duration += call_duration

    def add_busy_drop(self) -> None:
        with self._lock:
            self.busy_drops += 1

    def snapshot(self) -> dict[str, Any]:
        with self._lock:
            # ⚡ Bolt: Removed O(N log N) sorted() since Python dicts maintain insertion order,
            # and dictionary is pre-allocated sequentially. Reduces snapshot overhead.
            return {
                "freshers": {
                    str(i): dict(stats)
                    for i, stats in self.fresher_statistics.items()
                },
                "technical_lead": {
                    "counter": self.technical_lead_counter,
                    "call_duration": self.technical_lead_call_duration,
                },
                "project_manager": {
                    "counter": self.project_manager_counter,
                    "call_duration": self.project_manager_call_duration,
                },
                "busy_drops": self.busy_drops,
            }

    def print_summary(self) -> None:
        data = self.snapshot()
        print("----------------------------------------------")
        print("Summary:")
        for i, stats in data["freshers"].items():
            print(
                f"fresher {int(i) + 1}: answered {stats['counter']} calls "
                f"and spent {stats['call_duration']} seconds on the phone."
            )
        tl = data["technical_lead"]
        pm = data["project_manager"]
        print(
            f"Technical lead: answered {tl['counter']} calls "
            f"and spent {tl['call_duration']} seconds on the phone."
        )
        print(
            f"Project manager: answered {pm['counter']} calls "
            f"and spent {pm['call_duration']} seconds on the phone."
        )
        print(f"Busy drops: {data['busy_drops']}")
