## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-06-01 - Unbounded time intervals risk
**Vulnerability:** The simulation allowed unbounded `min_max_sleep_interval` and `min_max_call_duration`, which could cause long-running blocking operations leading to resource exhaustion (DoS).
**Learning:** For threaded simulations using `time.sleep`, allowing users to provide arbitrarily large durations can block threads or main process indefinitely.
**Prevention:** Always enforce explicit upper bounds (e.g. `<= 86400` seconds) on any time or sleep intervals based on external configuration to prevent unbounded blocking.
