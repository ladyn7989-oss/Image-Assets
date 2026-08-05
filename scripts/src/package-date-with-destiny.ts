import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "../..");
const sourcePath = path.join(
  root,
  "attached_assets/date-with-destiny_1785900001839.html",
);
const publicImages = path.join(
  root,
  "artifacts/mockup-sandbox/public/images/date-with-destiny",
);
const source = fs.readFileSync(sourcePath, "utf8");
const imageNames = new Set(
  fs
    .readdirSync(publicImages)
    .filter((name) => /\.(png|jpe?g|webp|gif)$/i.test(name)),
);
const tempRoot = fs.mkdtempSync(path.join(os.tmpdir(), "date-with-destiny-"));

const readme = {
  offline: `# Date With Destiny — Offline Edition

This archive is generated from the current game source and bundled artwork.

Extract the ZIP completely, keep index.html beside the images folder, and open index.html in a modern browser. No internet connection or server is required.

Saves and settings use browser local storage. If direct file storage is restricted, run python3 -m http.server 8000 in the extracted folder.
`,
  online: `# Date With Destiny — Online Edition

This archive is generated from the current game source. Original remote artwork URLs remain enabled, while filename-only assets are bundled locally.

Extract the ZIP and open index.html in a modern browser.
`,
  mobile: `# Date With Destiny — Mobile Offline Edition

This archive contains one self-contained index.html with the current game source and all artwork embedded directly. Extract it and open index.html on a modern mobile browser.
`,
};

function basename(value: string) {
  return value.split("?", 1)[0].replace(/\/+$/, "").split("/").pop() ?? value;
}

function rewriteImages(html: string, mode: "offline" | "online" | "mobile") {
  const imageReference = /(["'])([^"']+\.(?:png|jpe?g|webp|gif))\1/gi;
  const missing = new Set<string>();
  const rewritten = html.replace(imageReference, (full, quote, value) => {
    const name = basename(value);
    if (!imageNames.has(name)) return full;
    if (mode === "online" && /^https?:\/\//i.test(value)) return full;
    if (mode === "mobile") {
      const data = fs.readFileSync(path.join(publicImages, name)).toString("base64");
      const mime = name.toLowerCase().endsWith(".jpg")
        ? "jpeg"
        : name.toLowerCase().endsWith(".webp")
          ? "webp"
          : name.toLowerCase().endsWith(".gif")
            ? "gif"
            : "png";
      return `${quote}data:image/${mime};base64,${data}${quote}`;
    }
    return `${quote}images/${name}${quote}`;
  });

  for (const match of rewritten.matchAll(imageReference)) {
    const value = match[2];
    if (
      !/^https?:\/\//i.test(value) &&
      !value.startsWith("data:") &&
      !value.startsWith("images/")
    ) {
      missing.add(value);
    }
  }
  assert.deepEqual([...missing], [], `${mode} archive has no unresolved local image references`);
  return rewritten;
}

function run(command: string, args: string[]) {
  execFileSync(command, args, { cwd: root, stdio: "inherit" });
}

function writeZip(
  archiveName: string,
  entries: Array<{ source?: string; archive: string; content?: string }>,
) {
  const staging = path.join(tempRoot, archiveName.replace(/\.zip$/, ""));
  fs.mkdirSync(staging, { recursive: true });
  for (const entry of entries) {
    const destination = path.join(staging, entry.archive);
    fs.mkdirSync(path.dirname(destination), { recursive: true });
    if (entry.source) fs.copyFileSync(entry.source, destination);
    else fs.writeFileSync(destination, entry.content ?? "");
  }
  const archivePath = path.join(root, archiveName);
  fs.rmSync(archivePath, { force: true });
  execFileSync("zip", ["-q", "-r", "-9", archivePath, "."], {
    cwd: staging,
    stdio: "inherit",
  });
}

function imageEntries() {
  return [...imageNames].sort().map((name) => ({
    source: path.join(publicImages, name),
    archive: `images/${name}`,
  }));
}

function buildGameArchives() {
  writeZip("date-with-destiny-offline.zip", [
    { archive: "README.md", content: readme.offline },
    { archive: "index.html", content: rewriteImages(source, "offline") },
    ...imageEntries(),
  ]);
  writeZip("date-with-destiny-online.zip", [
    { archive: "README.md", content: readme.online },
    { archive: "index.html", content: rewriteImages(source, "online") },
    ...imageEntries(),
  ]);
  writeZip("date-with-destiny-mobile-offline.zip", [
    { archive: "README.md", content: readme.mobile },
    { archive: "index.html", content: rewriteImages(source, "mobile") },
  ]);
}

function buildSpriteArchive() {
  const archiveName = "date-with-destiny-new-character-sprites.zip";
  const staging = path.join(tempRoot, "sprites");
  fs.mkdirSync(staging, { recursive: true });
  const oldArchive = path.join(root, archiveName);
  assert.ok(fs.existsSync(oldArchive), `${archiveName} is required for its manifest and references`);
  run("unzip", ["-q", "-j", oldArchive, "MANIFEST.json", "README.md", "-d", staging]);
  for (const character of ["aether", "luna", "wolf"]) {
    const input = path.join(root, "attached_assets/generated_images", `${character}-new`);
    for (const file of fs.readdirSync(input).filter((name) => name.endsWith(".png"))) {
      const destination = path.join(staging, character, file);
      fs.mkdirSync(path.dirname(destination), { recursive: true });
      fs.copyFileSync(path.join(input, file), destination);
    }
  }
  const archivePath = path.join(root, archiveName);
  fs.rmSync(archivePath, { force: true });
  execFileSync("zip", ["-q", "-r", "-9", archivePath, "."], {
    cwd: staging,
    stdio: "inherit",
  });
}

function verifyArchives() {
  const expected = [
    ["date-with-destiny-offline.zip", ["index.html", "README.md", "images/aether-new-neutral.png"]],
    ["date-with-destiny-online.zip", ["index.html", "README.md", "images/luna-new-neutral.png"]],
    ["date-with-destiny-mobile-offline.zip", ["index.html", "README.md"]],
    ["date-with-destiny-new-character-sprites.zip", ["MANIFEST.json", "aether/neutral.png", "luna/neutral.png", "wolf/neutral.png"]],
  ] as const;
  for (const [archive, entries] of expected) {
    const listing = execFileSync("unzip", ["-Z1", path.join(root, archive)], {
      encoding: "utf8",
    });
    for (const entry of entries) {
      assert.ok(listing.split("\n").includes(entry), `${archive} contains ${entry}`);
    }
  }
}

try {
  buildGameArchives();
  buildSpriteArchive();
  verifyArchives();
  console.log("Date With Destiny archives rebuilt and verified.");
} finally {
  fs.rmSync(tempRoot, { recursive: true, force: true });
}