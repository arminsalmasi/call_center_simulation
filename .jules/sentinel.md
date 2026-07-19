## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-06-15 - Unbounded CLI Input DoS Risk
**Vulnerability:** The CLI argument parser in `call_center_simulation.py` accepted unbounded inputs for `number_of_freshers`, `run_time`, etc., leading to resource exhaustion or long blocking loops despite internal validation constraints.
**Learning:** Argument parsing must enforce strict upper limits (e.g., maximum threads <= 1000) at the entry point to ensure graceful failure with `parser.error()` before object instantiation is attempted.
**Prevention:** Always validate both upper bounds and valid ranges directly within CLI `argparse` configurations before passing data to inner application logic.
