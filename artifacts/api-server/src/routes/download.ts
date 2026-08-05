import { Router, type IRouter } from "express";
import path from "node:path";

const router: IRouter = Router();
const archivePath = path.resolve(
  import.meta.dirname,
  "../../../date-with-destiny-offline.zip",
);
const onlineArchivePath = path.resolve(
  import.meta.dirname,
  "../../../date-with-destiny-online.zip",
);
const mobileOfflineArchivePath = path.resolve(
  import.meta.dirname,
  "../../../date-with-destiny-mobile-offline.zip",
);
const fullSpriteArchivePath = path.resolve(
  import.meta.dirname,
  "../../../wolf-luna-aether-full-sprites.zip",
);

router.get("/download/date-with-destiny-offline.zip", (_req, res) => {
  res.download(
    archivePath,
    "date-with-destiny-offline.zip",
    {
      headers: {
        "Cache-Control": "no-store",
      },
    },
    (error) => {
      if (error && !res.headersSent) {
        res.status(404).json({
          error: "Download not available",
        });
      }
    },
  );
});

router.get("/download/date-with-destiny-online.zip", (_req, res) => {
  res.download(
    onlineArchivePath,
    "date-with-destiny-online.zip",
    {
      headers: {
        "Cache-Control": "no-store",
      },
    },
    (error) => {
      if (error && !res.headersSent) {
        res.status(404).json({
          error: "Download not available",
        });
      }
    },
  );
});

router.get("/download/date-with-destiny-mobile-offline.zip", (_req, res) => {
  res.download(
    mobileOfflineArchivePath,
    "date-with-destiny-mobile-offline.zip",
    {
      headers: {
        "Cache-Control": "no-store",
      },
    },
    (error) => {
      if (error && !res.headersSent) {
        res.status(404).json({
          error: "Download not available",
        });
      }
    },
  );
});

router.get("/download/wolf-luna-aether-full-sprites.zip", (_req, res) => {
  res.download(
    fullSpriteArchivePath,
    "wolf-luna-aether-full-sprites.zip",
    {
      headers: {
        "Cache-Control": "no-store",
      },
    },
    (error) => {
      if (error && !res.headersSent) {
        res.status(404).json({
          error: "Download not available",
        });
      }
    },
  );
});

export default router;