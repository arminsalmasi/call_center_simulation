## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-24 - Enforce Independent CLI Input Boundaries with `parser.error()`
**Vulnerability:** The CLI script threw raw Unhandled Exceptions (stack traces) and was vulnerable to Resource Exhaustion (DoS) due to unbounded thread creation/sleeps that were only caught deep in a class's inner `set` method instead of failing cleanly during parameter parsing.
**Learning:** When using `argparse` for CLI inputs, always independently validate user input constraints and upper bounds (using `parser.error()`) even if inner class methods enforce them.
**Prevention:** Implement strict range boundaries during CLI ingestion to ensure inputs gracefully fail without stack traces and immediately block bounded resource exhaustion via Thread Limits.
