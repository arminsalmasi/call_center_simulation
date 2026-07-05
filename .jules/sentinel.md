## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-24 - Prevent CPU Spinning DoS in Continuous Loops
**Vulnerability:** CPU spinning/DoS loop due to allowing a 0 sleep interval between simulation waves.
**Learning:** Validating for non-negative values (`>= 0`) is insufficient when dealing with `time.sleep()` in continuous `while True:` loops. A zero sleep interval causes the loop to spin wildly, consuming 100% CPU.
**Prevention:** Always enforce a strictly positive lower bound (`> 0`) for sleep intervals in continuous simulation loops to prevent resource exhaustion.
