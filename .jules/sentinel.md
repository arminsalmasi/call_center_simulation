## 2024-05-18 - Missing Input Validation on Thread Simulation

**Vulnerability:** The simulation lacked input bounds checking, meaning an attacker could specify massive numbers of threads (`number_of_freshers`) causing resource exhaustion/DoS, or specify negative/inconsistent arguments leading to runtime crashes.
**Learning:** Simulations with parameters derived directly from external input must be defensively guarded, particularly when thread creation correlates directly with one of the input integers.
**Prevention:** Always implement input validation and constraints on API or command line inputs that define system state sizes (like the number of threads or simulation length) before initializing those states.
