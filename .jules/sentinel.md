## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2026-06-19 - Unbounded CLI Arguments Risk
**Vulnerability:** Resource Exhaustion (DoS) risk due to unbounded `argparse` inputs in `call_center_simulation.py`, allowing unbounded thread creation and indefinitely long blocking operations.
**Learning:** Inner class parameter validations (if they exist) aren't enough when CLI inputs directly dictate memory allocation (e.g. `number_of_freshers` spawning threads) and execution durations. Without explicit upper limits, malicious or malformed input can easily cause the simulation to consume all memory or hang.
**Prevention:** Always enforce explicit, sane upper bounds on CLI parameters during `argparse` validation using `parser.error()` before instantiating objects or running loops, even if those values are logically "valid" lower down.
