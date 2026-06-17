## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-23 - Prevent Resource Exhaustion via Argument Bounds
**Vulnerability:** The `call_center_simulation.py` script accepted CLI arguments for thread counts and sleep/run intervals without upper bounds. An attacker or errant user could provide massive inputs (e.g., `number_of_freshers=1000000`), leading to unbounded thread creation and Denal of Service (DoS) by resource exhaustion.
**Learning:** Unbounded integers passed directly to application resource allocators (like thread pool size or time durations) pose a severe DoS risk, even in local CLI tools if they process untrusted input or run in shared environments.
**Prevention:** Always enforce explicit upper bounds and valid range checks on user-provided arguments, especially when those arguments dictate resource allocation or execution timing.
