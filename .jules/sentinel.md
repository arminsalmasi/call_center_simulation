## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-06-23 - Missing Upper Bounds for Thread Creation Parameters
**Vulnerability:** The simulation script lacked explicit upper limits for parameters like `number_of_freshers`, `run_time`, `max_calls_per_wave`, `max_sleep_interval`, and `max_call_duration`. This allows for unbounded thread creation and long-running blocking operations, which can lead to Resource Exhaustion (Denial of Service).
**Learning:** Even internal or local simulation scripts need bounds checking. An attacker or even a simple typo could crash the system or consume excessive resources if user input dictates resource allocation without limits.
**Prevention:** Always enforce explicit upper bounds and range checks during input validation (e.g., in `argparse` validation blocks) to prevent uncontrolled resource usage.
