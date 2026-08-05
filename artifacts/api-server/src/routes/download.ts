import { Router, type IRouter } from "express";
import path from "node:path";

const router: IRouter = Router();
const archivePath = path.resolve(
  import.meta.dirname,
  "../../../date-with-destiny-offline.zip",
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

export default router;