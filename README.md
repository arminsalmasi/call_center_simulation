# Call Center Simulation

Free-threaded Python call-center simulator with a CLI and a small FastAPI live dashboard.

Incoming calls are routed to idle **freshers**, then the **technical lead**, then the **project manager**. If everyone is busy, the call is dropped and counted.

## Requirements

- macOS/Linux with Homebrew (recommended) or another free-threaded CPython install
- **Free-threaded CPython 3.14+** so the GIL can stay disabled
  - Homebrew: `brew install python-freethreading` (provides `python3.14t`)
- `pip` (comes with the venv)

On a free-threaded build, the GIL is already off. You can still force it with `PYTHON_GIL=0` or `python -X gil=0`.

## Environment setup

From the repository root:

```bash
# 1. Install free-threaded Python (once per machine)
brew install python-freethreading

# 2. Create and activate a virtualenv with that interpreter
python3.14t -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 3. Install project dependencies
pip install -r requirements.txt

# 4. Confirm the GIL is disabled
python -c "import sys; assert not sys._is_gil_enabled(); print('GIL disabled')"
```

Deactivate later with `deactivate`.

## How to run

### CLI simulation

```bash
source .venv/bin/activate

python -m call_center.cli 3 5 1 3 1 2 1 2 --seed 42
# equivalent shim:
python call_center_simulation.py 3 5 1 3 1 2 1 2 --seed 42
```

Positional arguments (all integers except `--seed` is optional):

| # | Argument | Meaning |
|---|----------|---------|
| 1 | `number_of_freshers` | Fresher agents (1–1000) |
| 2 | `run_time` | Simulation length in seconds |
| 3–4 | `min_calls` / `max_calls` | Calls per wave |
| 5–6 | `min_sleep` / `max_sleep` | Seconds between waves (`max_sleep` must be > 0) |
| 7–8 | `min_duration` / `max_duration` | Call length in seconds |
| — | `--seed N` | Optional RNG seed for reproducible runs |

Programmatic example (see also `test.py`):

```python
from call_center import CallCenterSimulation

sim = CallCenterSimulation()
sim.set(3, 5, (1, 3), (1, 2), (1, 2), seed=42)
sim.run_simulation()
```

### Web dashboard

```bash
source .venv/bin/activate
PYTHON_GIL=0 uvicorn web.app:app --host 127.0.0.1 --port 8000
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000). Use the form to start/stop a simulation, watch agent idle/busy state, live stats, and the SSE event log.

API endpoints:

- `GET /` — dashboard HTML
- `POST /api/simulation/start` — JSON body with simulation params
- `POST /api/simulation/stop`
- `GET /api/simulation/status` — JSON snapshot
- `GET /api/simulation/events` — Server-Sent Events stream

### Tests

```bash
source .venv/bin/activate
pytest -q
```

## Project layout

```
call_center/          # simulation package
  models.py           # Agent idle/busy state machine
  router.py           # fresher → TL → PM routing
  stats.py            # thread-safe CallStatistics
  events.py           # in-process EventBus for UI
  engine.py           # CallCenterSimulation orchestration
  validation.py       # single input-bounds module
  cli.py              # argparse entrypoint
web/                  # FastAPI app + templates/static
tests/                # pytest suite
call_center_simulation.py   # thin compatibility shim
requirements.txt
pyproject.toml
```

## Architecture notes

- Agents keep a stable identity (`idle` / `busy`). Each call runs on a **new** daemon thread (Python threads cannot be restarted).
- Shared stats and routing use locks so free-threading stays correct.
- Wave waits are interruptible; finishing calls uses `Condition.wait` instead of a busy spin.
- More detail: [documentation.md](documentation.md)
