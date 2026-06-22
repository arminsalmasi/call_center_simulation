## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-06-22 - Resource Exhaustion (DoS) via Unbounded CLI Parameters
**Vulnerability:** The simulation's command-line interface lacked upper bounds for critical parameters such as the number of freshers (threads), run time, and maximum calls per wave, which could lead to unbounded thread creation or excessively long execution times (Resource Exhaustion/DoS) when the script is run with maliciously large arguments.
**Learning:** Even internal or local CLI applications can cause system instability if parameters controlling thread creation or long-running tasks are unconstrained.
**Prevention:** Always implement explicit upper bounds for CLI arguments controlling resources, system processes, or thread counts, validating them early with `parser.error()`.
