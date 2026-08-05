---
name: Uploaded classic-script interactions
description: Safe extension pattern for self-contained uploaded HTML games executed inside the React mockup wrapper.
---

When extending an uploaded self-contained game whose event dispatcher is minified into a long classic-script line, keep the original dispatcher intact and intercept only new actions with a document-level capture-phase listener.

**Why:** Line-based edits against a minified dispatcher are brittle and can accidentally change unrelated original game behavior. A capture listener can handle new `data-a` actions before the legacy target listeners without rebuilding the game.

**How to apply:** Add the interception after the original script has initialized and bound its controls. Call `preventDefault()` and `stopImmediatePropagation()`, update the shared state, persist it, and rerender. Keep automatic/world rules in the original logic unless the requested behavior explicitly changes them.