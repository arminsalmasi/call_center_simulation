## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-05-25 - Unhandled Exception Exposure via CLI
**Vulnerability:** Missing upper bounds checks in CLI argument parsing allowed unhandled `ValueError` exceptions to bubble up from inner methods, leaking stack traces.
**Learning:** Relying solely on inner class method validation for CLI arguments leads to ungraceful failures and potential information leakage when users provide invalid bounds.
**Prevention:** Always independently validate user input constraints and upper bounds at the CLI boundary (using `parser.error()`) to ensure a clean exit.
