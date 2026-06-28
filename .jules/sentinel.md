## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-05-24 - DoS Prevention via Strict Bounds
**Vulnerability:** Missing explicit upper bounds on sleep/call intervals and non-positive lower bounds on freshers/run_time in the simulation parameters allowed for potential Resource Exhaustion (DoS) and functional bugs.
**Learning:** Even internal class methods need explicit upper bounds for all resource-related parameters. CLI argument parsers must also independently validate these constraints to prevent unhandled exceptions and ensure graceful failure.
**Prevention:** Always enforce both strictly positive lower bounds (> 0) and explicit upper bounds (e.g., <= 86400) for simulation parameters across both the argparse level and the internal set() methods.
