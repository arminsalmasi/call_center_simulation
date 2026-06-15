## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-24 - Unbounded Resource Exhaustion (DoS)
**Vulnerability:** The CLI application allowed an unbounded number of freshers and unlimited sleep/run intervals, which could lead to excessive thread creation and memory exhaustion (Denial of Service).
**Learning:** Even local CLI applications should enforce upper bounds on inputs that control thread creation, memory allocation, or unbounded waiting periods.
**Prevention:** Always validate configuration parameters with strict upper limits at the input boundaries (e.g., in `argparse` configuration) to fail securely before processing begins.
