## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-07-06 - Prevent CPU Spinning / DoS via zero sleep intervals
**Vulnerability:** The simulation's parameters permitted a (0, 0) sleep interval, which causes the main loop to not sleep at all, leading to CPU spinning and potential resource exhaustion (Denial of Service).
**Learning:** Even internal tool arguments should be strictly validated against unbounded usage or extreme resource constraints that could lead to DoS conditions.
**Prevention:** Ensure configurable intervals or delays have a strictly positive upper bound to enforce minimum wait times when resolving tasks in continuous loops.
