## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-24 - Unhandled Exception DoS via CLI Inputs

**Vulnerability:** The command-line `argparse` configuration in `main()` lacked upper bound checks on integers. If bounded inputs were given, the script threw a raw `ValueError` stack trace rather than exiting cleanly.
**Learning:** For defense in depth, validation constraints (like max thread counts or interval lengths) should be explicitly duplicated at the CLI parsing layer. Relying solely on inner class exceptions can lead to unexpected program crashes or uncaught error traces.
**Prevention:** Always use `parser.error()` in `argparse` validation blocks to validate upper bounds independently, ensuring a graceful fail state before passing inputs to inner logic.
