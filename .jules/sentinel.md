## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-24 - Missing Input Validation DoS risk (Part 2)

**Vulnerability:** The CLI arguments in `main()` lacked explicit upper bounds (e.g. for `run_time`, `max_sleep_interval`, `max_call_duration`), which could still allow resource exhaustion despite inner class checking due to unhandled exceptions.
**Learning:** For CLI inputs parsed with `argparse`, independently validate user input constraints and upper bounds using `parser.error()` even if inner class methods enforce them. This ensures a clean exit (graceful failure) rather than throwing internal unhandled exceptions when receiving invalid inputs.
**Prevention:** Enforce strict explicit upper bounds (e.g. `args.run_time <= 86400`) during argument validation for user-supplied intervals to mitigate DoS via long-running blocking operations.
