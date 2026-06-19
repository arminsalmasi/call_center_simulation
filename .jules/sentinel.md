## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-06-19 - Unhandled Exception DoS Risk via Argparse

**Vulnerability:** The argparse configuration lacked independent upper bound checks for numeric inputs (like thread counts or time limits), delegating validation entirely to inner class methods.
**Learning:** If argparse passes out-of-bound inputs, the inner class will throw unhandled exceptions (e.g. ValueError) causing stack trace leaks and dirty exits rather than graceful failure.
**Prevention:** Always implement independent upper bound constraints and range validations within the argparse setup (using `parser.error()`) to ensure the application exits cleanly on malicious or erroneous input.
