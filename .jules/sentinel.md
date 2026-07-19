## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-05-24 - Unhandled Exceptions via Argparse Missing Upper Bounds
**Vulnerability:** The argparse implementation in `main()` lacked independent validation of upper bounds for thread counts and limits, relying entirely on inner class validation that raises unhandled `ValueError` exceptions upon invalid input.
**Learning:** When using `argparse` for CLI inputs, independently validate user input constraints and upper bounds (using `parser.error()`) even if inner class methods enforce them. This prevents unhandled exceptions and ensures a clean exit (graceful failure) when receiving invalid inputs.
**Prevention:** Always implement parallel, robust validation directly in the CLI parsing layer to fail gracefully before application logic initialization.
