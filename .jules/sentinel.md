## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-05-24 - [Resource Exhaustion]
**Vulnerability:** The simulation CLI lacked upper bounds for its thread pool sizing and interval delays (`number_of_freshers`, `run_time`, etc.), which could theoretically lead to Resource Exhaustion (DoS) through unbounded thread creation or extremely long sleep durations if malicious or erroneous inputs were passed.
**Learning:** Argument validation without explicit upper caps is insufficient. Even if logic within the simulation behaves correctly, accepting unbounded input strings implicitly allows massive allocations that stress OS limits.
**Prevention:** Always enforce strict and explicit upper bounds (e.g., maximum limits like 1000 for thread counts, 86400 for temporal limits) during input parsing alongside lower bounds before allocating thread pools or executing blocking delays.
