## 2024-05-23 - Prevent thread exhaustion DoS in Call Center Simulation
**Vulnerability:** The `CallCenterSimulation.set()` method lacked bounds checking on `number_of_freshers` and input constraints, which could lead to resource/thread exhaustion DoS.
**Learning:** Simulations with uncontrolled parameters can cause excessive thread instantiation leading to system instability, crashing, and lack of responsiveness.
**Prevention:** Always implement strong input validation/limits on parameters directly controlling thread creation or long-running loops.
