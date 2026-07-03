## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-07-03 - Strict Positive Lower Bounds for Sleep Intervals
**Vulnerability:** Core API allowed a zero value for `min_max_sleep_interval`, causing the main simulation loop to spin rapidly on CPU without yielding, leading to Resource Exhaustion (DoS).
**Learning:** Allowing '0' in configuration checks (e.g., `0 <= limit <= 1000`) for sleep durations that control the rate of infinite or long-running loops can introduce CPU exhaustion vulnerabilities.
**Prevention:** Always use strictly positive lower bounds (e.g., `0 < limit <= 1000`) when validating core operational configuration variables like sleep intervals.
