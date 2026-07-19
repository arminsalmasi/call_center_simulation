## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-05-24 - Missing Input Validation DoS risk (Part 2: Sleep/Duration Limits)

**Vulnerability:** The parameters `min_max_sleep_interval`, `min_max_call_duration`, and their CLI counterparts lacked upper bounds, which could lead to resource exhaustion and long-running blocks in simulations due to untrusted/excessive user input.
**Learning:** Whenever dealing with sleep and duration logic, inputs must be bounded not just at lower bounds (e.g., `>= 0`) but explicitly at logical upper bounds (e.g., `<= 86400` representing 1 day) to protect execution environments from DoS scenarios.
**Prevention:** Apply strict positive and maximum constraints on all CLI and setup parameters mapping to system delays or thread sleeps.
