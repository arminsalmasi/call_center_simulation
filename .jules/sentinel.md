## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2026-05-31 - Unbounded Thread Creation and Resource Exhaustion Risk
**Vulnerability:** The CLI arguments for `number_of_freshers`, `run_time`, `max_sleep_interval`, and `max_call_duration` lacked explicit upper bounds, allowing an attacker to specify extremely large values leading to Resource Exhaustion (DoS) via unbounded thread creation or excessively long blocking operations.
**Learning:** Command-line inputs that dictate the number of threads created or the duration of blocking operations must always be strictly validated and bounded to prevent excessive system resource consumption.
**Prevention:** Always enforce explicit upper bounds and valid range checks on parameters directly influencing resource allocation or long-running operations.
