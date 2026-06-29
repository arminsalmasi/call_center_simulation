## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-06-29 - Missing Upper Bounds for Blocking Operations

**Vulnerability:** Sleep intervals and call durations lacked explicit upper bounds in both `CallCenterSimulation.set()` and the CLI arguments, risking long-running blocking operations and thread exhaustion DoS.
**Learning:** Thread-based operations relying on user-provided time inputs (like `time.sleep()`) require strict upper limits (e.g., `<= 86400` seconds) to prevent unrecoverable stalls. Additionally, independent bounds validation in CLI arguments is required to fail gracefully instead of crashing with unhandled exceptions.
**Prevention:** Always enforce positive lower bounds and explicit upper bounds on any user-controlled delay or looping parameter at both the CLI entry point (`argparse`) and core simulation logic.
