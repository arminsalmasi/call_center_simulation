## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-06-14 - Missing CLI Arguments DoS Risk

**Vulnerability:** The CLI argument parser in `call_center_simulation.py` lacked explicit upper bounds checks for inputs like `number_of_freshers`, allowing unbounded thread creation via command line.
**Learning:** Even if inner class methods validate parameters, `argparse` needs explicit independent validation to prevent unhandled exceptions and ensure a clean exit (graceful failure) when users provide maliciously large inputs directly.
**Prevention:** Always independently validate user input constraints and upper bounds (using `parser.error()`) alongside internal constraints for defense in depth.
