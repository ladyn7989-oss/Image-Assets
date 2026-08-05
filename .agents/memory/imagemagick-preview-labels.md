---
name: ImageMagick preview labels
description: Workspace-specific behavior when creating labeled image contact sheets
---

ImageMagick `montage` can fail while rendering filename labels when the workspace has no configured font, even though the source images are valid.

**Why:** A labeled preview is optional and should not block packaging generated image assets.

**How to apply:** Omit `-label` and text annotations for contact sheets in this workspace, or use a known installed font only after verifying it exists.