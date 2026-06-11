## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-24 - Missing CLI Input Validation DoS risk

**Vulnerability:** The CLI inputs in `main()` lacked upper bounds validations (e.g. `number_of_freshers <= 1000`), allowing unbounded thread creation or long simulation duration inputs to trigger a `ValueError` bubble up from the internal `CallCenterSimulation.set()` method, crashing the application ungracefully.
**Learning:** Python multithreaded simulations taking user-supplied inputs must validate constraints independently at the edge/entry point (like `argparse`) using correct parser fail patterns (`parser.error()`) to ensure graceful failure, instead of relying solely on inner class method unhandled exceptions.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating list or configuring run-times based on external CLI configuration.
