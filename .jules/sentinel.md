## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-05-30 - Prevent Resource Exhaustion (DoS) via Explicit CLI Validation
**Vulnerability:** The simulation application accepted inputs via `argparse` without independent upper bound checks in the main execution block. Although inner methods (like `CallCenterSimulation.set`) raised `ValueError` exceptions, unbounded inputs directly passed to threading operations or resulting in uncaught exceptions create a Denial of Service (DoS) risk.
**Learning:** Inner class validation is insufficient for CLI scripts. Unhandled `ValueError` exceptions cause stack traces and poor user experiences, and unbounded input directly into simulation parameters can exhaust system resources (e.g., unlimited threads).
**Prevention:** Always add explicit upper boundary validations (e.g., max threads <= 1000, max intervals <= 86400) directly in the CLI argument parsing block using `parser.error()` before initializing business logic objects. This ensures a secure, clean exit (graceful failure) when receiving invalid inputs.
