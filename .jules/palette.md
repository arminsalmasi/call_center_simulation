## 2024-12-14 - Button State Conflicts
**Learning:** When managing loading states manually in a DOM where state is also periodically overridden by polling (e.g. renderStatus), disabling elements during async operations like fetch() can lead to permanently disabled buttons if an early network or HTTP error occurs before the poll resets it.
**Action:** Always wrap fetch() calls in a try-catch block to handle exceptions and explicitly re-enable buttons on early errors.
