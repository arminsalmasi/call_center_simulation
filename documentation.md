# Call Center Simulation — Documentation

This project simulates a call center with concurrent agents on **free-threaded CPython**. Calls arrive in waves and are routed to the first available agent in this order:

1. Fresher  
2. Technical lead  
3. Project manager  
4. If all are busy → drop the call (`busy_drops`)

The same engine powers the **CLI** and the **FastAPI** dashboard.

For install and run commands, see [README.md](README.md).

---

## Design

### Agents (`call_center/models.py`)

- `Agent` is a stable object with role `fresher` | `technical_lead` | `project_manager`.
- State machine: `idle` ↔ `busy`, guarded by a `Lock` / `Condition`.
- `try_assign()` claims an idle agent, picks a call duration from the configured range, starts a **new** daemon thread to sleep for that duration, then returns to `idle` and emits events.
- Threads are not reused (Python cannot restart a thread); the agent object is reused.

### Routing (`call_center/router.py`)

`Router.route_call()` tries each fresher, then the technical lead, then the project manager. Outcomes: `FRESHER`, `TECHNICAL_LEAD`, `PROJECT_MANAGER`, or `BUSY`.

### Statistics (`call_center/stats.py`)

Thread-safe counters and total durations per fresher index, technical lead, project manager, plus `busy_drops`. `snapshot()` returns JSON-friendly data; `print_summary()` prints the CLI end report.

### Events (`call_center/events.py`)

In-process `EventBus` fans out `SimulationEvent` values (`wave`, `call_assigned`, `call_finished`, `busy`, `started`, `finished`, …) to subscriber queues. The web UI uses this for Server-Sent Events (SSE).

### Engine (`call_center/engine.py`)

`CallCenterSimulation`:

- `set(...)` / `SimulationConfig.create(...)` validate and store parameters (optional `seed`).
- `run_simulation(background=False)` runs the wave loop; `background=True` starts a daemon runner thread (used by the web app).
- `stop()` requests interruption of wave sleeps and joins the runner when waiting.
- `status_snapshot()` returns status, config, agent states, stats, and recent events.

Wave loop: until `run_time` elapses or stop is requested → random call count → route each call → interruptible sleep until the next wave → wait for agents to become idle via `Condition.wait` → print summary.

### Validation (`call_center/validation.py`)

Single source of bounds (e.g. freshers 1–1000, run time ≤ 86400, sleep max > 0). Used by CLI and the web API so limits stay consistent.

### CLI (`call_center/cli.py`)

`python -m call_center.cli …` parses eight positional ints plus optional `--seed`, validates, and runs the simulation.

### Compatibility shim (`call_center_simulation.py`)

Re-exports `CallCenterSimulation`, `CallStatistics`, `main`, etc., so older imports and scripts keep working.

### Web app (`web/app.py`)

FastAPI app with one in-process simulation instance:

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/` | HTML dashboard |
| POST | `/api/simulation/start` | Start with JSON config |
| POST | `/api/simulation/stop` | Request stop |
| GET | `/api/simulation/status` | JSON snapshot |
| GET | `/api/simulation/events` | SSE stream |

Templates live under `web/templates/`; static assets under `web/static/`.

---

## Environment setup

```bash
brew install python-freethreading
python3.14t -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -c "import sys; assert not sys._is_gil_enabled(); print('GIL disabled')"
```

Dependencies are listed in `requirements.txt` and `pyproject.toml` (FastAPI, Uvicorn, Jinja2, httpx, pytest).

---

## How to run

### CLI

```bash
source .venv/bin/activate
python -m call_center.cli 8 60 1 5 2 5 10 20 --seed 1
```

Meaning: 8 freshers, 60s run, 1–5 calls/wave, 2–5s between waves, 10–20s call duration.

### Programmatic

```python
from call_center import CallCenterSimulation

sim = CallCenterSimulation()
sim.set(
    number_of_freshers=3,
    run_time=20,
    min_max_calls_per_wave=(1, 3),
    min_max_sleep_interval=(5, 6),
    min_max_call_duration=(5, 10),
    seed=42,
)
sim.run_simulation()
```

Also see `test.py` (short demo) and `stress.py` (heavier load).

### Web dashboard

```bash
source .venv/bin/activate
PYTHON_GIL=0 uvicorn web.app:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000.

### Tests

```bash
source .venv/bin/activate
pytest -q
```

Coverage includes stats concurrency smoke, router escalation, engine with mocked sleep, GIL-off check on free-threaded builds, and FastAPI start/status/stop.

---

## Parameter bounds (summary)

| Parameter | Constraint |
|-----------|------------|
| `number_of_freshers` | 1 … 1000 |
| `run_time` | (0, 86400] seconds (float allowed for web demos) |
| calls per wave | 0 ≤ min ≤ max ≤ 10000 |
| sleep interval | 0 ≤ min ≤ max ≤ 86400 and **max > 0** |
| call duration | 0 ≤ min ≤ max ≤ 86400 |

Invalid values raise `TypeError` / `ValueError` (CLI surfaces them via argparse).

---

## Free-threading notes

- Use `python3.14t` (or another build with `Py_GIL_DISABLED`).
- Verify with `sys._is_gil_enabled() is False`.
- Workload is mostly timed waits; locks still protect shared stats and agent state so the design remains correct when the GIL is off.
