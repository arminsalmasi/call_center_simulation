## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-06-20 - Missing CLI Argument Upper Bounds

**Vulnerability:** The simulation script lacked upper bound checks on CLI arguments (e.g. number of freshers, run time, intervals) in the argparse config.

**Learning:** This missing check could lead to a Resource Exhaustion (DoS) vulnerability by allowing unbounded thread creation or excessively long-running sleep/blocking operations prior to the internal bounds being checked, leading to uncaught ValueErrors.

**Prevention:** Always enforce explicit upper bounds directly in the CLI parser level as well to ensure the app fails gracefully and catches invalid inputs at the boundary.
