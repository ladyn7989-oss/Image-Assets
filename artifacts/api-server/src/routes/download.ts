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

export default router;