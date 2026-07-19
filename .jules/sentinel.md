## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-06-02 - Resource Exhaustion (DoS) due to Unbounded Input Parameters
**Vulnerability:** The simulation allowed users to specify unbounded input parameters (e.g., unlimited number of freshers/threads, arbitrarily large run times and sleep intervals up to infinity), leading to excessive resource consumption, thread starvation, or application crashes resulting in a Denial of Service.
**Learning:** For long-running simulation applications or those that accept CLI input to create threads, relying on default validation (checking simply `> 0`) is insufficient. The absence of explicit upper bounds creates an implicit vulnerability when those values are mapped to system-level objects or sleep timers.
**Prevention:** Always enforce explicit, strict upper boundaries on input sizes that dictate resource allocation. In this project, enforce a maximum of 1000 for user thread counts (freshers) and a logical maximum constraint like `86400` (1 day in seconds) for timers/sleep durations and `10000` for call wave capacities.
