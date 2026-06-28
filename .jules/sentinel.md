## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-06-28 - Enforce strictly positive lower bounds
**Vulnerability:** Zero bounds permitted in loop structures
**Learning:** Maintaining exactly zero for lower bounds in thread instantiations or timeouts risks generating infinite loops or division by zero cases.
**Prevention:** Always maintain strictly positive lower bounds (> 0) for core simulation parameters.
