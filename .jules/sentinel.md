## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2026-05-28 - Missing Thread Join Timeouts
**Vulnerability:** Unbounded `while True:` loops waiting for threads to finish without a timeout logic, exposing the system to Denial of Service (DoS) risks via resource exhaustion if a thread hangs.
**Learning:** Simulation loops waiting for threads or state changes must always have an upper bound timeout safety net to avoid infinite spin-locks.
**Prevention:** Always use a bounding time mechanism (e.g. `timeout_end = time.time() + MAX_WAIT` and `if time.time() > timeout_end: break`) when implementing custom `while True:` synchronization barriers for threads.
