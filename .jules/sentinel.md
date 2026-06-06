## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-06-06 - Prevent DoS via Resource Exhaustion
**Vulnerability:** The CLI arguments for the call center simulation lacked upper bound validation, allowing an attacker to input extremely large values (e.g., millions of freshers or extremely long run times). This could lead to a Denial of Service (DoS) via resource exhaustion (e.g., creating too many threads, leading to memory/CPU exhaustion).
**Learning:** Even internal or seemingly safe simulation tools can be vulnerable to DoS if input validation is incomplete. Always validate both lower and upper bounds for inputs that dictate resource allocation (like thread counts or loop iterations).
**Prevention:** Explicitly enforce valid upper limits (e.g., `number_of_freshers <= 1000`, `run_time <= 86400`) during argument parsing using `parser.error()` before instantiating objects or running loops.
