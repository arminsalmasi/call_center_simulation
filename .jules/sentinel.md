## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-06-14 - Independent CLI Argument Validation
**Vulnerability:** Resource Exhaustion (DoS risk) via unbounded CLI input parameters (e.g., massive thread creation due to `number_of_freshers`, or long execution blocking via `run_time`).
**Learning:** Even if inner class methods (`CallCenterSimulation.set()`) validate limits, `argparse` CLI inputs must independently validate user constraints and upper bounds (using `parser.error()`). This ensures clean exits and prevents unhandled exceptions when users provide out-of-bounds parameters.
**Prevention:** Always enforce explicit upper bounds directly in CLI argument parsers before initializing or invoking core application logic.
