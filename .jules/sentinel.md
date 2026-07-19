## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-24 - Unhandled Exceptions on Invalid CLI Input
**Vulnerability:** Unhandled exceptions due to relying on inner class methods for CLI input validation.
**Learning:** In this CLI application, failing to independently validate argparse upper bounds leads to unhandled exceptions instead of graceful exits.
**Prevention:** Always validate user input constraints and upper bounds at the argparse level even if inner classes enforce them.
