---
name: Uploaded HTML image packaging
description: Reliable image handling for uploaded self-contained HTML pages rendered inside the mockup sandbox.
---

When an uploaded HTML page references hosted images or bare filenames, package the hosted originals under the mockup sandbox public image directory and rewrite all references to the sandbox image URL. Add a safe fallback for unresolved bare filenames.

**Why:** Uploaded pages often depend on private, expiring, or cross-origin media hosts; bare filenames also do not resolve from the sandbox preview. Keeping the originals local makes the visual result deterministic and prevents broken-image states.

**How to apply:** Preserve the uploaded page's scripts and markup, transform only its asset URLs at preview load time, and use the mockup sandbox's `/__mockup/images/` path for packaged assets.