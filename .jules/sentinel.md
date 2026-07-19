## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2025-02-27 - Unbounded CLI Arguments DoS Risk
**Vulnerability:** The CLI application parsed arguments like `number_of_freshers` and `run_time` but lacked upper bound enforcement, making it trivial for a user or automated system to trigger memory exhaustion or excessive execution time by providing massively out-of-bounds input parameters.
**Learning:** Argument parsing using `argparse` needs explicit independent upper bound checks (`> MAX_VALUE: parser.error()`) to safely terminate invalid input states before hitting internal logic limits.
**Prevention:** Always define explicit thresholds on numeric CLI parameters before instantiating internal classes or running application logic to avoid Resource Exhaustion and ensure a graceful fallback.
