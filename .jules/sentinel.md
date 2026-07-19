## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-05-24 - CLI Input Validation Graceful Exit
**Vulnerability:** The `argparse` configuration in `main()` lacked explicit upper boundary validation, relying instead on inner class error handling which led to unhandled exceptions and messy crashes.
**Learning:** Argument parsing scripts should independently validate user input constraints and upper bounds using `parser.error()` before initializing the main classes.
**Prevention:** Always implement max boundary checks and invalid range validation directly within the `argparse` configuration block so the application can exit cleanly with a clear error message.
