## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-25 - Resource Exhaustion DoS vulnerability via CLI Arguments

**Vulnerability:** The `argparse` configuration in `main()` did not properly cap input values, meaning that maliciously large integers for `number_of_freshers`, `run_time`, or `max_calls_per_wave` could bypass argparse type-checks and cause out-of-memory or CPU starvation before being safely rejected by the application logic.
**Learning:** Argument parsers must validate constraints (e.g., `< 1000`) before they are passed down to deeper simulation layers, especially in heavily threaded or computational systems. Furthermore, using a `try-except` structure to gracefully reject values directly with `parser.error` is cleaner than raising an untracked exception.
**Prevention:** Add hard upper-bounds validation within the argument parsing phase and wrap downstream programmatic configuration in handled exception blocks.
