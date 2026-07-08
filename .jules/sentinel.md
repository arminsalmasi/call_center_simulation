## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-05-24 - CPU Spinning DoS Vulnerability
**Vulnerability:** The simulation allowed `min_max_sleep_interval` to be set to `(0, 0)`, which could cause an infinite loop with no delay, leading to CPU spinning and Denial of Service.
**Learning:** Continuous `while True` loops in multithreaded Python applications must enforce strictly positive sleep intervals to prevent thread starvation and 100% CPU utilization.
**Prevention:** Always ensure upper bounds for loop sleep intervals are `> 0` during input validation to guarantee the event loop yields CPU time.
