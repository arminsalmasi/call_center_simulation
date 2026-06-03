## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-06-03 - Unbounded thread sleep interval DoS risk
**Vulnerability:** The `min_max_sleep_interval` and `min_max_call_duration` parameters in the CLI argument parser and `CallCenterSimulation.set()` lacked explicit maximum upper bounds, allowing unbounded thread sleep and resource blocking.
**Learning:** Python threading simulations accepting user inputs for sleep intervals and timeouts must have explicit maximum limits enforced. Otherwise, malicious input can block threads indefinitely, leading to a Resource Exhaustion DoS condition.
**Prevention:** Always enforce upper bounds (e.g. `<= 86400` seconds / 1 day) and valid ranges on external configurations determining thread wait times or blocking operations.
