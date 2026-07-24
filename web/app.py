"""Minimal FastAPI dashboard for the call center simulation."""

from __future__ import annotations

import asyncio
import json
import queue
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from call_center.engine import CallCenterSimulation
from call_center.validation import validate_simulation_params

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

app = FastAPI(title="Call Center Simulation")

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    """
    Security Enhancement: Add standard security headers to all responses.
    - CSP mitigates XSS by restricting resource loading.
    - X-Content-Type-Options prevents MIME-sniffing.
    - X-Frame-Options prevents Clickjacking.
    - Referrer-Policy protects referral info.
    - Strict-Transport-Security enforces secure connections.
    """
    response = await call_next(request)
    response.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response

_manager_lock = __import__("threading").Lock()
_simulation = CallCenterSimulation()


class StartRequest(BaseModel):
    number_of_freshers: int = Field(default=3, ge=1, le=1000)
    run_time: float = Field(default=10, gt=0, le=86400)
    min_calls_per_wave: int = Field(default=1, ge=0)
    max_calls_per_wave: int = Field(default=3, ge=0)
    min_sleep_interval: int = Field(default=1, ge=0)
    max_sleep_interval: int = Field(default=2, gt=0)
    min_call_duration: int = Field(default=1, ge=0)
    max_call_duration: int = Field(default=2, ge=0)
    seed: int | None = None


def get_simulation() -> CallCenterSimulation:
    return _simulation


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "index.html",
        {"title": "Call Center Simulation"},
    )


@app.get("/api/simulation/status")
def status() -> dict[str, Any]:
    return get_simulation().status_snapshot()


@app.post("/api/simulation/start")
def start(body: StartRequest) -> dict[str, Any]:
    sim = get_simulation()
    with _manager_lock:
        if sim.status_snapshot()["status"] == "running":
            raise HTTPException(status_code=409, detail="Simulation already running")
        try:
            sim.set(
                body.number_of_freshers,
                body.run_time,
                (body.min_calls_per_wave, body.max_calls_per_wave),
                (body.min_sleep_interval, body.max_sleep_interval),
                (body.min_call_duration, body.max_call_duration),
                seed=body.seed,
            )
        except (TypeError, ValueError) as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc

        sim.run_simulation(background=True)
    return {"ok": True, "status": sim.status_snapshot()}


@app.post("/api/simulation/stop")
def stop() -> dict[str, Any]:
    sim = get_simulation()
    sim.stop(wait=False)
    return {"ok": True, "status": sim.status_snapshot()}


@app.get("/api/simulation/events")
async def events(request: Request) -> StreamingResponse:
    sim = get_simulation()
    q = sim.event_bus.subscribe()

    async def generate():
        try:
            yield f"data: {json.dumps({'kind': 'connected', 'message': 'subscribed'})}\n\n"
            keepalive_counter = 0
            while True:
                if await request.is_disconnected():
                    break
                try:
                    # Security: Non-blocking check with async sleep prevents thread pool exhaustion DoS
                    item = q.get_nowait()
                    keepalive_counter = 0
                except queue.Empty:
                    await asyncio.sleep(0.5)
                    keepalive_counter += 1
                    if keepalive_counter >= 30: # 15 seconds
                        yield ": keepalive\n\n"
                        keepalive_counter = 0
                    continue
                if item is None:
                    yield f"data: {json.dumps({'kind': 'closed', 'message': 'stream closed'})}\n\n"
                    break
                yield f"data: {json.dumps(item.to_dict())}\n\n"
        finally:
            sim.event_bus.unsubscribe(q)

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


def main() -> None:
    import os

    import uvicorn

    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "8000"))
    uvicorn.run("web.app:app", host=host, port=port, reload=False)


if __name__ == "__main__":
    main()
