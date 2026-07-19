## 2024-05-22 - [Missing Input Validation in Simulation Arguments]
**Vulnerability:** Application crashed or hung leading to potential resource exhaustion (DoS) when providing malformed simulation bounds (e.g. negative time limits, bounds where min > max, huge number of freshers).
**Learning:** Simulation setup methods receiving unverified CLI arguments must validate ranges, types, and strict constraints before instantiating massive numbers of threads.
**Prevention:** Implement guard clauses explicitly verifying boundary conditions early in the configuration logic rather than relying on underlying modules (like `secrets.SystemRandom().randint`) to throw obscure failures.
