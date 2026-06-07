## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-28 - Missing CLI Upper Bounds Checks (DoS Risk)

**Vulnerability:** The simulation script lacked validation upper bounds on critical CLI inputs like `max_sleep_interval`, `max_call_duration`, and `max_calls_per_wave`, exposing the system to potential Resource Exhaustion (DoS) through unbound thread execution or indefinitely blocking sleep cycles.
**Learning:** Python multithreaded and timing-sensitive applications taking user-supplied inputs must have explicit, hardcoded upper limits independently validated at both the `argparse` configuration layer (for graceful CLI failure) and inside business logic methods to prevent malicious inputs blocking the application.
**Prevention:** Always implement max boundary constraints (e.g., `<= 86400` seconds) on external inputs controlling application lifetimes, threading, or sleep routines to prevent indefinite hangs or process limit exhaustion.
