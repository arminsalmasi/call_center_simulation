## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-18 - Missing CLI Upper Bounds Causing Unhandled Exceptions
**Vulnerability:** Missing explicit upper bounds in `argparse` validation logic for CLI inputs, even when inner class methods enforce them.
**Learning:** Inner class validation prevents the actual Resource Exhaustion but leads to unhandled `ValueError` exceptions being thrown instead of a graceful CLI exit via `parser.error()`.
**Prevention:** Always independently validate user input constraints and upper bounds (using `parser.error()`) within the CLI interface before passing data to inner logic.
