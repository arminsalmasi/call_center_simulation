## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-05-24 - Unhandled Exceptions Leaking Stack Traces (DoS edge case)
**Vulnerability:** The CLI application leaked internal `ValueError` stack traces when given arguments violating maximum bounds because validation was only handled deep in the class logic rather than the `argparse` configuration.
**Learning:** For public or internal CLI tools, exposing raw Python stack traces is bad practice. In addition, delaying validation allows potentially unbounded inputs to leak deeper into class structures.
**Prevention:** When using `argparse` for CLI input, ALWAYS independently validate user input constraints and upper bounds (using `parser.error()`) to ensure a clean exit and graceful failure state.
