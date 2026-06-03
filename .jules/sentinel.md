## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-05-24 - Unbounded Sleep Interval DoS risk
**Vulnerability:** The `CallCenterSimulation.set()` and `main()` methods lacked upper bound input validation for `min_max_sleep_interval` and `min_max_call_duration`, allowing a user to specify extremely large sleep durations (e.g., years) which could block threads or the main execution indefinitely, leading to resource exhaustion.
**Learning:** Python multithreaded simulations relying on user-provided values for `time.sleep()` need explicit upper bound checks to prevent threads from hanging permanently and consuming system resources without yielding.
**Prevention:** Always enforce upper boundaries (e.g., `<= 86400` seconds) on time-related arguments, especially sleep durations and timeouts, in both library APIs and CLI parsing validation.
