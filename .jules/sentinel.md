## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2025-02-27 - CLI Input Validation Missing Explicit Bounds

**Vulnerability:** The argparse configuration in `main()` lacked explicit upper bounds checks for multiple arguments, allowing potentially dangerous inputs to reach the core simulation classes.
**Learning:** For CLI tools, argument parsing must independently enforce the same upper bounds constraints as the internal methods to fail fast and gracefully via `parser.error()`.
**Prevention:** Always mirror the internal input validations (both lower and upper bounds) in the `argparse` configuration of the CLI entry point.
