## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-06-12 - Prevent Resource Exhaustion (DoS) via Unbounded Thread Creation
**Vulnerability:** The CLI arguments used to start the simulation lacked upper bounds. This allowed a malicious or erroneous user to input arbitrarily large numbers (e.g., millions of freshers or extremely long sleep/call intervals) which could lead to unbounded thread creation, causing memory exhaustion and blocking application operations (DoS).
**Learning:** Application limits and constraints should always be checked independently of logical code execution boundaries (e.g., using `argparse` configuration) to ensure a clean exit (`parser.error()`) without consuming resources or attempting execution that leads to unhandled exceptions.
**Prevention:** Always add maximum boundary constraints alongside minimum checks for all numeric input parameters that dictate resource allocation (like threads or loop bounds).
