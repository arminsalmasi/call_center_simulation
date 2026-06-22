## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-05-24 - Unhandled Exceptions & CLI Bounds Bypass

**Vulnerability:** Even if inner class methods (`CallCenterSimulation.set()`) validate bounds, missing identical validation in CLI entrypoints (`main()` argparse) causes Python to throw messy unhandled stack trace exceptions when limits are exceeded, rather than exiting gracefully, and risks DoS if outer layers pass unbounded data before inner classes instantiate.
**Learning:** Always duplicate valid ranges and strict upper bounds in argparse validators independently of core class checks to guarantee graceful CLI exit and block unbounded resources as early as possible.
**Prevention:** Add explicit upper bound constraints (e.g. `> 10000`, `> 86400`) mapping to core validation limits directly within `argparse` using `parser.error()`.
