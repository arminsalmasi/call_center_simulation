## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-06-09 - Missing CLI Argument Bounds leading to DoS Risk
**Vulnerability:** The `argparse` configuration in `main()` of `call_center_simulation.py` lacked strict upper bounds for user inputs like `number_of_freshers`, allowing unbounded thread creation causing DoS risk. The validation relied partially on inner class functions which raised exceptions instead of gracefully exiting the CLI.
**Learning:** Python multithreaded CLI simulations taking user-supplied configuration must enforce maximum bounds directly at the CLI input parsing level (using `parser.error()`) to ensure graceful failure.
**Prevention:** Always add maximum boundaries and valid range checks when creating lists or starting threads based on external configuration using `argparse`. Ensure that errors are caught early to prevent unhandled exceptions.
