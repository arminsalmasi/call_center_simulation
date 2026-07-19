## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-07-04 - Zero-Sleep CPU Spinning DoS risk
**Vulnerability:** The simulation allowed `min_max_sleep_interval` to have a lower bound of `0`, which could cause infinite/spinning while loops that consume all available CPU.
**Learning:** Simulation loops that rely on dynamic sleep durations must explicitly enforce strictly positive lower bounds (`> 0`) to prevent intentional or accidental denial of service (DoS) through resource exhaustion.
**Prevention:** Always use strictly positive (`> 0`) validation checks for sleep intervals that throttle main event loops.
