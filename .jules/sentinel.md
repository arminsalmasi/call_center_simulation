## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-23 - Prevent DoS from CPU Spinning in Simulation Loops
**Vulnerability:** A missing strictly positive upper bound on random time intervals (`min_max_sleep_interval[1]`) allowed a configuration of `(0, 0)`, causing `time.sleep(0)` inside a `while True` loop and leading to a CPU-spinning Denial of Service (DoS) exhaustion of resources.
**Learning:** In continuous simulations, allowing a maximum interval of 0 for random sleep generation can lead to uncontrolled loop iterations.
**Prevention:** Always enforce a strictly positive upper bound (`> 0`) on random time delays used in `time.sleep()` within infinite or time-based loops.
