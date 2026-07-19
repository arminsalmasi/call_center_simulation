## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-06-21 - Unhandled Exception / Resource Exhaustion via Unbounded CLI Args

**Vulnerability:** The CLI argument parser in `call_center_simulation.py` accepted unbound user inputs for simulation parameters like `max_calls_per_wave` and `max_call_duration`.
**Learning:** Argument bounds and validity constraints must be verified locally at the CLI `argparse` level using `parser.error()`, even if inner classes eventually throw ValueErrors.
**Prevention:** Always mirror or implement stricter upper bounds checking in CLI parsers to prevent unhandled exceptions and potential denial-of-service before instantiating backend classes.
