## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-06-23 - Prevent Resource Exhaustion (DoS) via Unbounded Thread Creation
**Vulnerability:** The `argparse` configuration in `call_center_simulation.py` lacked explicit upper bounds checks for critical parameters like `number_of_freshers`, `run_time`, `max_sleep_interval`, and `max_call_duration`. This allowed for unbounded thread creation and excessively long execution times, leading to a Resource Exhaustion Denial of Service (DoS) vulnerability.
**Learning:** Even if inner class methods enforce constraints, CLI inputs (`argparse`) must independently validate bounds. Large inputs for thread creation or simulation time parameters can trivially exhaust system resources, freeze execution, or cause crashes.
**Prevention:** Always enforce explicit, reasonable upper bounds (e.g., maximum freshers <= 1000, time/sleep intervals <= 86400) and proper range checks directly within the input validation layer (like `argparse`) before instantiating objects or spawning threads.
