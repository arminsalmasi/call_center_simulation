## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-24 - Missing CLI Upper Bounds DoS Risk
**Vulnerability:** The argparse CLI arguments lacked upper bounds, leading to unhandled `ValueError` exceptions from inner class validation instead of a graceful exit, or potential Resource Exhaustion DoS if bypassed.
**Learning:** Always validate input constraints and upper bounds at the earliest entry point (CLI argument parsing using `parser.error()`) to ensure graceful failure and prevent unhandled exceptions.
**Prevention:** Add explicit upper bounds and constraints checks using `parser.error()` when parsing CLI arguments.
