---
name: Standalone game bundles
description: Packaging rule for uploaded HTML games with downloadable standalone archives.
---

Standalone ZIPs are snapshots, not live views of the uploaded HTML or preview asset directory. Any source or bundled-art change requires rebuilding the relevant offline, online, mobile, and sprite archives, then checking their download routes. The repository now has a checked-in package command for this.

**Why:** The mockup preview can be current while previously generated archives still contain older game logic or artwork.

**How to apply:** Run `pnpm package:date-with-destiny` from the repository root after source or asset changes; it rebuilds and verifies the archives. Inspect representative contents and request each registered download endpoint before delivery.