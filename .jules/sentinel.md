## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-06-20 - Unbounded Thread Creation Risk via CLI Args
**Vulnerability:** Resource Exhaustion (DoS). The CLI allowed arbitrary large numbers of threads (`number_of_freshers`) and unconstrained simulated parameters like run times or call lengths without explicit upper bounds. This allows attackers (or accidental inputs) to cause memory exhaustion or excessively long-running processes that hold resources hostage.
**Learning:** Argument validation focused only on the absolute minimum constraints (e.g., `> 0`) but forgot to consider resource constraints by not capping the maximum limits.
**Prevention:** Always enforce logical and resource-based upper bounds for all CLI parameters (e.g. `maximum freshers <= 1000`, `time/sleep intervals <= 86400`) during `argparse` validation to ensure gracefully failing rather than processing dangerous inputs.
