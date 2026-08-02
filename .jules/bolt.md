## 2024-08-02 - Avoid dataclasses.asdict for frequent serialization
**Learning:** In highly active event streams (like `call_center/events.py`), `dataclasses.asdict` becomes a significant CPU bottleneck because it recursively traverses and deep-copies elements while using reflection, rather than simple attribute access.
**Action:** Replace `asdict` with a manually constructed dictionary literal (e.g. `{'kind': self.kind...}`) for performance-critical serialization.
