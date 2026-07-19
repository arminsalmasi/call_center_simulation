## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-06-04 - Unhandled Exceptions during Argparse Lead to Denial of Service
**Vulnerability:** The CLI arguments in `call_center_simulation.py` lacked explicit upper bounds (e.g. for max connections, duration).
**Learning:** If upper bounds are not validated during `argparse` processing, deeply nested logic or class validation may raise exceptions (e.g., ValueError) that are not gracefully handled by the top-level script, resulting in application crashes and DoS vulnerabilities.
**Prevention:** Always validate both lower and upper bounds independently within the input parsing phase (using `parser.error()`) to ensure clean exits and prevent Resource Exhaustion (DoS).
