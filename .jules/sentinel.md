## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-06-06 - Resource Exhaustion DoS risk in CLI

**Vulnerability:** The CLI arguments lacked explicit upper bound validation, allowing unbounded resource usage (DoS risk) by users executing the simulation script.
**Learning:** `argparse` types only provide basic type conversion; explicit upper bounds checks should be implemented independently in the CLI layer using `parser.error()` to ensure graceful failure.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000` for threads, `<= 86400` for time) using `parser.error()` when parsing CLI arguments.
