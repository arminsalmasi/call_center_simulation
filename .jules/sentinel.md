## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2026-05-31 - Unbounded Parameters Leading to Resource Exhaustion (DoS)
**Vulnerability:** Simulation parameters (`min_max_sleep_interval` and `min_max_call_duration`) lacked upper bounds.
**Learning:** This oversight could result in excessively long sleep durations or blocking operations, allowing a user to effectively perform a DoS attack on the simulation threads by passing arbitrarily large integers via arguments.
**Prevention:** Always enforce explicit upper bounds on input configuration values (like timeouts, intervals, and freshers) to constrain process execution time and prevent unbounded blocking operations.
