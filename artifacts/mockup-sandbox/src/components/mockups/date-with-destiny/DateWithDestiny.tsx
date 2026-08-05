import { useEffect, useRef } from "react";

import sourceHtml from "../../../../../../attached_assets/date-with-destiny_1785900001839.html?raw";

const imageRoot = "/__mockup/images/date-with-destiny/";
const fallbackImage = `${imageRoot}49cab3afa_generated_image.png`;

function makePreviewSafe(html: string): string {
  return html.replace(
    /https?:\/\/[^"'\\\s]+\/([^"'\\\s/]+(?:\.png|\.jpe?g|\.webp|\.gif))/gi,
    (_match, filename: string) => `${imageRoot}${filename}`,
  ).replace(
    /(["'])(?:fomo\.png|riko\.webp|nyx-bellweather\.png)\1/gi,
    `$1${fallbackImage}$1`,
  );
}

export function DateWithDestiny() {
  const rootRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const root = rootRef.current;
    if (!root) return;

    const html = makePreviewSafe(sourceHtml);
    const styleText = html.match(/<style[^>]*>([\s\S]*?)<\/style>/i)?.[1] ?? "";
    const scriptText = html.match(/<script[^>]*>([\s\S]*?)<\/script>/i)?.[1] ?? "";
    const style = document.createElement("style");
    style.dataset.preview = "date-with-destiny";
    style.textContent = styleText;
    document.head.appendChild(style);

    root.innerHTML = '<div id="g"></div>';
    const safeScript = `${scriptText}
      document.querySelectorAll("#g img").forEach(function (img) {
        img.addEventListener("error", function () {
          if (img.getAttribute("src") !== "${fallbackImage}") {
            img.setAttribute("src", "${fallbackImage}");
          }
        });
      });
    `;

    try {
      // The uploaded page is a self-contained classic script. Running it in a
      // Function preserves its original non-module behavior and interactions.
      new Function(safeScript)();
    } catch (error) {
      root.innerHTML = `<pre style="padding:16px;color:#fecaca;background:#1a0e2e;white-space:pre-wrap">${String(error)}</pre>`;
    }

    return () => {
      style.remove();
      root.innerHTML = "";
    };
  }, []);

  return <div ref={rootRef} style={{ minHeight: "100dvh" }} />;
}