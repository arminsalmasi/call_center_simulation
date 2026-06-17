## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.
## 2024-06-25 - Prevent Unbounded Resource Allocation before Class Initialization

**Vulnerability:** The CLI arguments lacked explicit upper bounds checks, allowing arbitrarily large input values (like `number_of_freshers=2000`) to be passed from the CLI before failing deep inside the domain logic, representing a risk for resource exhaustion or unbounded allocations prior to domain instantiation.
**Learning:** For application entrypoints (like `argparse`), upper bounds input validation must be done explicitly to fail gracefully and securely as soon as possible, independently of inner domain rules.
**Prevention:** Always add explicit maximum boundary checks directly inside `argparse` validation to stop unbounded inputs before domain objects are created or initialized.
