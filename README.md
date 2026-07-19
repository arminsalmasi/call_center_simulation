# Call Center Simulation

Free-threaded Python call-center simulator with a small FastAPI live dashboard.

## Requirements

- Free-threaded CPython 3.14+ (Homebrew: `brew install python-freethreading` → `python3.14t`)
- Optional: run with `PYTHON_GIL=0` / `python -X gil=0` (already the default on `python3.14t`)

## Setup

```bash
python3.14t -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Confirm the GIL is off:

```bash
python -c "import sys; assert not sys._is_gil_enabled(); print('GIL disabled')"
```

## CLI

```bash
python -m call_center.cli 3 5 1 3 1 2 1 2 --seed 42
# or
python call_center_simulation.py 3 5 1 3 1 2 1 2 --seed 42
```

Args: `freshers run_time min_calls max_calls min_sleep max_sleep min_duration max_duration`.

## Web dashboard

```bash
PYTHON_GIL=0 uvicorn web.app:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000 — start/stop the simulation, watch agent idle/busy state, stats, and SSE events.

## Tests

```bash
pytest -q
```

## Architecture

- `call_center/` — models (idle/busy agents), router, stats, event bus, engine, CLI validation
- `web/` — FastAPI UI + SSE
- Agents keep a stable identity; each call runs on a new daemon thread (threads cannot restart)
- Shared stats/router state is lock-guarded so free-threading stays correct
