## 2026-05-20 - Unbounded Inputs Causing Denial of Service
**Vulnerability:** The `CallCenterSimulation.set()` method accepts unbounded inputs for variables such as `number_of_freshers`, leading to potential Denial of Service (DoS) attacks or severe resource exhaustion during thread creation (a `Fresher` inherits from `Thread`).
**Learning:** Simulations initializing numerous threads or loops driven directly by unverified user input are high-risk points for systemic stability. Thread-based architectures crash fast on unbounded resource allocation.
**Prevention:** Always enforce strict boundaries on inputs that drive resource allocations, loops, and object creation, such as capping the maximum number of instances (e.g., maximum threads).
