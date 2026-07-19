"""Compatibility shim for the legacy module path."""

from call_center.cli import main
from call_center.engine import CallCenterSimulation, SimulationConfig
from call_center.models import Agent, AgentState, Role
from call_center.stats import CallStatistics

__all__ = [
    "Agent",
    "AgentState",
    "CallCenterSimulation",
    "CallStatistics",
    "Role",
    "SimulationConfig",
    "main",
]

if __name__ == "__main__":
    raise SystemExit(main())
