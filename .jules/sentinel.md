## 2024-05-24 - Missing Input Validation DoS risk

**Vulnerability:** The `CallCenterSimulation.set()` method lacked input validation for `number_of_freshers`, allowing unbounded thread creation.
**Learning:** Python multithreaded simulations taking user-supplied thread counts need explicit bounds checks to prevent memory exhaustion and OS process limits blocking.
**Prevention:** Always add maximum boundaries (e.g. `<= 1000`) and valid range checks when creating lists or starting threads based on external configuration.

## 2024-05-25 - CPU Spinning DoS in Simulation Loops
**Vulnerability:** The simulation loop allowed a sleep interval of 0, which could cause a CPU spinning Denial of Service (DoS) loop.
**Learning:** Simulation loops without strictly positive sleep intervals can consume 100% CPU and block other processes when sleep parameters are derived from user input.
**Prevention:** Always enforce a strictly positive lower bound (`> 0`) on sleep or wait intervals in continuous `while True` simulation loops.
