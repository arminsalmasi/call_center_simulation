"""FastAPI dashboard tests."""

from fastapi.testclient import TestClient

from web.app import app, get_simulation


client = TestClient(app)


def test_index_renders():
    res = client.get("/")
    assert res.status_code == 200
    assert "Call Center Simulation" in res.text


def test_start_status_stop_flow():
    sim = get_simulation()
    if sim.status_snapshot()["status"] == "running":
        sim.stop(wait=True)

    start = client.post(
        "/api/simulation/start",
        json={
            "number_of_freshers": 2,
            "run_time": 0.5,
            "min_calls_per_wave": 1,
            "max_calls_per_wave": 1,
            "min_sleep_interval": 1,
            "max_sleep_interval": 1,
            "min_call_duration": 0,
            "max_call_duration": 0,
            "seed": 7,
        },
    )
    assert start.status_code == 200, start.text
    status = client.get("/api/simulation/status")
    assert status.status_code == 200
    body = status.json()
    assert body["status"] in {"running", "finished", "stopped"}
    assert "agents" in body

    stop = client.post("/api/simulation/stop")
    assert stop.status_code == 200


def test_start_rejects_invalid_payload():
    res = client.post(
        "/api/simulation/start",
        json={
            "number_of_freshers": 0,
            "run_time": 1,
            "min_calls_per_wave": 1,
            "max_calls_per_wave": 1,
            "min_sleep_interval": 0,
            "max_sleep_interval": 0,
            "min_call_duration": 1,
            "max_call_duration": 1,
        },
    )
    assert res.status_code in {400, 422}
