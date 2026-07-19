## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-24 - Missing Independent CLI Input Validation
**Vulnerability:** The CLI argument parsing in `main()` lacked upper bounds checks, potentially allowing unbounded inputs to be passed down and triggering inner class exceptions.
**Learning:** Unhandled exceptions from inner classes due to unvalidated CLI inputs can leak stack traces and fail ungracefully.
**Prevention:** Always independently validate user input constraints and upper bounds at the CLI parsing layer (using `parser.error()`) to ensure graceful failure and prevent unhandled exceptions.
