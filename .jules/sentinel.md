## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-07-05 - Missing Strictly Positive Lower Bound DoS risk

**Vulnerability:** The `min_max_sleep_interval` allowed a value of 0, which could lead to a `time.sleep(0)` tight loop, causing CPU spinning and a Denial of Service (DoS) risk.
**Learning:** Sleep intervals configured by external users must strictly prevent a 0-duration wait in continuous loops to prevent exhausting CPU resources.
**Prevention:** Always enforce a strictly positive lower bound (e.g., `> 0`) on inputs used for sleep intervals or delay configurations within unbounded or long-running loops.
