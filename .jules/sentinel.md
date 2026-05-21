## 2026-05-21 - [Input Validation Gap]
**Vulnerability:** Missing input validation in argparse allowed negative values and inverted bounds, enabling logic errors and infinite resource consumption.
**Learning:** Python CLI scripts using argparse don't automatically validate cross-argument logic (e.g., min > max) or negative inputs unless explicitly configured or checked.
**Prevention:** Always add post-parse validation blocks for bounds checking and logical constraints when using argparse to accept numeric thresholds.
