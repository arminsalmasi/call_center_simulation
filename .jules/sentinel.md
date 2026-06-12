## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-24 - Missing CLI Input Boundaries

**Vulnerability:** The CLI arguments parsed by `argparse` in `call_center_simulation.py` lacked strict upper boundaries, allowing unbounded values (like billions of freshers or extremely long run times).
**Learning:** Even if inner methods have validations (which were also bounded), outer boundaries should independently check against DoS by returning graceful failures (using `parser.error()`) rather than unhandled exceptions deep in the logic.
**Prevention:** Always add strict upper bound checks (e.g., `> 1000`, `> 86400`) when defining and parsing inputs with `argparse`.
