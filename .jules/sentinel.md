## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-06-27 - Argparse Input Validation and Unhandled Exception Prevention

**Vulnerability:** The CLI implementation relied exclusively on inner class methods for explicit boundary constraint checks, which throws a generic Python Exception (like ValueError) instead of exiting cleanly with an informative message.
**Learning:** Inner class boundary validation checks (like `if max > 86400: raise ValueError(...)`) are necessary for robustness, but if arguments are primarily supplied via `argparse`, those same boundaries should be duplicated at the CLI level using `parser.error()`. This ensures a graceful user exit (e.g. printing a standard "usage: ..." error and exiting with code 2) rather than dumping an unhandled stack trace to the user, which could potentially expose internal implementation paths.
**Prevention:** Always ensure that `argparse` explicitly enforces the complete set of upper and lower bounds defined by the core logic.
