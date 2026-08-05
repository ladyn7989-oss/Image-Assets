---
name: Copyright-safe game audio
description: Audio licensing and implementation rule for Date With Destiny.
---

The game uses an original procedural Web Audio ambient layer and short UI/belly tones rather than external music URLs.

**Why:** The game is distributed through standalone ZIPs, so unverified CDN music could create licensing, availability, and offline-play problems.

**How to apply:** Keep procedural audio as the default. Only bundle a recorded track after confirming and documenting a CC0 or public-domain license, and preserve the ambient/effects toggles and visibility pause behavior.