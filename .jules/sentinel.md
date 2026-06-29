## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-24 - Unbounded Time Intervals DoS Risk
**Vulnerability:** The simulation allowed arbitrarily large time intervals and durations via CLI inputs, leading to a Denial of Service (DoS) risk through resource exhaustion (e.g., hanging threads for extremely long periods).
**Learning:** In a multi-threaded CLI application, time-based inputs (like sleep intervals or call durations) must have strict, codebase-specific upper limits (e.g., <= 86400) enforced both at the parser level for graceful exit and within class initializations.
**Prevention:** Enforce strictly positive lower bounds (>0) and explicit upper limits (<= 86400) independently via `parser.error()` and within the inner class's initialization logic.
