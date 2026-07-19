## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-07-01 - Unhandled Exceptions via Missing CLI Upper Bounds
**Vulnerability:** The CLI `argparse` implementation lacked upper bound validation, causing large inputs to trigger unhandled `ValueError` exceptions deep within the application rather than gracefully exiting.
**Learning:** Inner class validation is insufficient for CLI applications if it leads to unhandled crashes. All constraints, especially resource limits (upper bounds), must be independently verified at the CLI boundary using `parser.error()` to ensure graceful failure.
**Prevention:** Always mirror internal bounds and constraint logic in the `argparse` layer (e.g., maximum thread counts and run times) to maintain application resilience and prevent exception-based crashes.
