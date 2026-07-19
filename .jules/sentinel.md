## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2025-02-12 - CLI Graceful Failure for Input Bounds

**Vulnerability:** The CLI arguments parsing for simulation limits in `call_center_simulation.py` lacked upper bound checks using `argparse`. This meant that out-of-bound arguments bypassed initial CLI validation, leading to unhandled exceptions raised deeper in the program (`CallCenterSimulation.set()`) instead of failing gracefully.
**Learning:** Even if inner classes perform validations, relying entirely on them for command-line inputs can cause unhandled stack traces rather than clean CLI failures.
**Prevention:** Always mirror input boundaries at the outermost boundary (the CLI parser) using `parser.error()` to ensure secure, graceful failures and good user experience.
