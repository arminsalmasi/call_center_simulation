"""Call routing: fresher → technical lead → project manager."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from call_center.models import Agent
from call_center.stats import CallStatistics


class RouteResult(str, Enum):
    FRESHER = "fresher"
    TECHNICAL_LEAD = "technical_lead"
    PROJECT_MANAGER = "project_manager"
    BUSY = "busy"


@dataclass
class RouteOutcome:
    result: RouteResult
    agent: Agent | None = None
    duration: int | None = None
    fresher_index: int | None = None


class Router:
    def __init__(
        self,
        freshers: list[Agent],
        technical_lead: Agent,
        project_manager: Agent,
        stats: CallStatistics,
    ) -> None:
        self.freshers = freshers
        self.technical_lead = technical_lead
        self.project_manager = project_manager
        self.stats = stats

    def route_call(self) -> RouteOutcome:
        for idx, fresher in enumerate(self.freshers):
            duration = fresher.try_assign()
            if duration is not None:
                self.stats.add_fresher_call(idx, duration)
                return RouteOutcome(
                    RouteResult.FRESHER,
                    agent=fresher,
                    duration=duration,
                    fresher_index=idx,
                )

        duration = self.technical_lead.try_assign()
        if duration is not None:
            self.stats.add_technical_lead_call(duration)
            return RouteOutcome(
                RouteResult.TECHNICAL_LEAD,
                agent=self.technical_lead,
                duration=duration,
            )

        duration = self.project_manager.try_assign()
        if duration is not None:
            self.stats.add_project_manager_call(duration)
            return RouteOutcome(
                RouteResult.PROJECT_MANAGER,
                agent=self.project_manager,
                duration=duration,
            )

        self.stats.add_busy_drop()
        return RouteOutcome(RouteResult.BUSY)
