---
name: Standalone game bundles
description: Packaging rule for uploaded HTML games with downloadable standalone archives.
---

Standalone ZIPs are snapshots, not live views of the uploaded HTML or preview asset directory. Any source or bundled-art change requires rebuilding the relevant offline, online, mobile, and sprite archives, then checking their download routes.

**Why:** The mockup preview can be current while previously generated archives still contain older game logic or artwork.

**How to apply:** Rebuild archives from the final source and asset set immediately before delivery; inspect representative archive contents and request each registered download endpoint.