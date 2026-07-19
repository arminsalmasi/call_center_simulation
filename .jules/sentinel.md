## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-25 - Unbounded Input DoS Vulnerability in CLI Arguments
**Vulnerability:** The CLI argument parser in `call_center_simulation.py` lacked upper bounds for user inputs (`number_of_freshers`, `run_time`, etc.), creating a DoS risk where excessively large inputs could lead to resource exhaustion (e.g., massive thread creation or unlimited sleep times).
**Learning:** Argument parsers must enforce strict upper limits, and independently validate user input constraints to gracefully fail and prevent unhandled exceptions downstream.
**Prevention:** Always implement explicit maximum boundary checks (e.g., `<= 1000` for threads, `<= 86400` for time) directly within the CLI parsing logic to catch invalid inputs early.
