## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The CLI arguments parsed by `main()` in `call_center_simulation.py` lacked explicit upper bounds checks (e.g., maximum freshers <= 1000), allowing bounded logic bypass and potentially unbounded thread creation / simulated resource exhaustion (DoS risk).
**Learning:** Even when standard library tools like `argparse` validate correct input types, domain-specific limit logic requires explicit bounds verification inside the script parsing phase.
**Prevention:** Always mirror or enforce explicit upper bounds from backend models to the CLI parsing configuration directly when handling multi-threaded parameters.
