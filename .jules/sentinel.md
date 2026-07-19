## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-30 - Unbounded Simulation Parameters DoS
**Vulnerability:** Resource Exhaustion (DoS) via unbounded simulation parameters.
**Learning:** ArgumentParser parameters were missing explicit upper bounds, allowing arbitrarily large values for thread counts and sleep intervals, which could crash the application or hang the system.
**Prevention:** Always enforce explicit upper bounds (e.g., maximum freshers <= 1000, time/sleep intervals <= 86400) on parameters that dictate resource allocation or long-running blocking operations.
