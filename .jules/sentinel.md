## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2026-05-28 - Unbounded Sleep DoS Vulnerability
**Vulnerability:** The `CallCenterSimulation.set()` method allowed arbitrarily large `min_max_sleep_interval` and `min_max_call_duration` values, enabling potential unbounded thread blocking/sleeping (Denial of Service).
**Learning:** For threaded simulations using randomized sleep intervals, external configurations must be strictly bounded to prevent process hangs and resource exhaustion, just like bounding the number of created threads.
**Prevention:** Enforce explicit maximum upper bounds (e.g., 86400 seconds / 1 day) on any external parameters passed to `time.sleep()` or similar blocking operations.
