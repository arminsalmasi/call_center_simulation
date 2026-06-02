## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-05-24 - Unbounded Time Intervals DoS Risk
**Vulnerability:** The parameters `min_max_sleep_interval` and `min_max_call_duration` lacked upper bounds checks, allowing arbitrarily long blocking operations (`time.sleep()`), leading to resource exhaustion and potential DoS.
**Learning:** Simulations relying on blocking I/O calls parameterized by user input must enforce strict upper boundaries (e.g., maximum 86400 seconds) to prevent prolonged resource locking.
**Prevention:** Always add maximum boundary conditions (e.g., `<= 86400`) alongside basic type checking when evaluating time intervals from external configuration.
