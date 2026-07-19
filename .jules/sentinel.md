## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-28 - Resource Exhaustion (DoS) risk from unbounded CLI inputs
**Vulnerability:** The simulation application accepted user inputs for thread counts (freshers) and timeout limits (run time, sleep interval, call duration) without enforcing upper bounds.
**Learning:** Even simple local simulation tools can be vulnerable to Resource Exhaustion (DoS) if they allocate system resources (like threads or sleep periods) based entirely on unbounded user input.
**Prevention:** Always enforce explicit and reasonable upper limits for resource-intensive inputs, particularly thread counts and blocking/timeout durations, even if they aren't part of a web request.
