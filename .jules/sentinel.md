## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-07-08 - CPU Spinning DoS risk
**Vulnerability:** The `min_max_sleep_interval` allowed a maximum of 0, which could cause a `(0, 0)` sleep interval, resulting in CPU spinning and a Denial of Service (DoS) loop.
**Learning:** Simulation loops that rely on random sleep intervals must enforce a strictly positive upper bound to ensure the loop actually sleeps and yields CPU.
**Prevention:** Always enforce `max > 0` for sleep intervals in continuous loops to prevent resource exhaustion.
## 2024-05-24 - Thread Pool Exhaustion DoS in FastAPI SSE
**Vulnerability:** Synchronous generator endpoints using `queue.get(timeout=...)` for SSE block FastAPI worker threads indefinitely, leading to unmitigated thread pool exhaustion DoS.
**Learning:** FastAPI assigns synchronous generators to its limited thread pool. Unbounded concurrent SSE connections will consume all threads, making the server unresponsive to other synchronous requests.
**Prevention:** Always use `async def` endpoints and asynchronous generators with non-blocking checks (e.g., `q.get_nowait()` and `await asyncio.sleep()`) for long-lived connections like SSE.
