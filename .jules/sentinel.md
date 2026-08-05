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
## 2024-07-24 - Overwritten FastAPI Security Headers Middleware
**Vulnerability:** Defining multiple HTTP middlewares in FastAPI that attempt to modify the same response headers will cause unintentional overwriting, as the first-defined middleware executes last. This can inadvertently weaken security rules, such as replacing a strict Content-Security-Policy with a more permissive one.
**Learning:** In FastAPI/Starlette, HTTP middlewares execute in the reverse order of their definition. Multiple middlewares affecting the same state (like headers) must be consolidated into a single middleware or carefully ordered to prevent regressions.
**Prevention:** Always consolidate security header additions into a single middleware function to ensure strict policies are applied and not silently overwritten by later executions.
## 2024-11-23 - CSP Strict Script Source
**Vulnerability:** The Content-Security-Policy header unnecessarily allowed 'unsafe-inline' for scripts despite no inline scripts being used in the application.
**Learning:** The frontend architecture dynamically renders the DOM using external scripts rather than inline blocks, permitting a stricter CSP for script sources.
**Prevention:** Always scope down CSP script-src to 'self' when an application's architecture does not rely on inline scripts, significantly mitigating XSS risks.
