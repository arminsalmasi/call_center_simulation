## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-05-24 - Zero-Duration Sleep Interval DoS Risk
**Vulnerability:** The `CallCenterSimulation.set()` method allowed (0, 0) sleep intervals, leading to immediate CPU spinning.
**Learning:** Simulation loops that rely on time intervals must explicitly validate non-zero upper bounds to prevent 100% CPU lockup and resource exhaustion.
**Prevention:** Always enforce a strictly positive upper bound for sleep or polling intervals in unbounded simulation loops.
