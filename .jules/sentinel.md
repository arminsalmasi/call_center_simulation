## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-06-18 - Unbounded CLI Arguments Cause Resource Exhaustion (DoS)
**Vulnerability:** The simulation's CLI arguments (`number_of_freshers`, time intervals, etc.) lacked explicitly enforced upper bounds, allowing an attacker to request millions of threads or incredibly long sleep/runtime durations.
**Learning:** This can lead to Resource Exhaustion (DoS) via unbounded thread creation or long-running blocking operations, crashing the application or server.
**Prevention:** Always enforce explicit upper bounds and valid range checks on CLI arguments, even if inner methods seem to handle them, to ensure graceful failure.
