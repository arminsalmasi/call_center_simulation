## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-06-27 - Unhandled Exception DoS Risk via Argparse

**Vulnerability:** The `argparse` configuration for `call_center_simulation.py` lacked explicit upper bound constraints, while inner classes implemented them. This mismatch allows large inputs to bypass initial CLI validation and crash the application with unhandled exceptions.
**Learning:** In CLI applications, external boundary inputs must be validated at the exact point of entry (`argparse` blocks) to prevent unhandled exceptions and enable graceful failures.
**Prevention:** Always mirror or strictly enforce internal business logic bounds inside the entry point's argument parser (e.g., using `parser.error()`) rather than relying on nested class initializations to throw errors.
