const CACHE_NAME = "date-with-destiny-preview-v1";

self.addEventListener("install", (event) => {
  event.waitUntil(self.skipWaiting());
});

self.addEventListener("activate", (event) => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener("fetch", (event) => {
  const request = event.request;
  const url = new URL(request.url);

  if (request.method !== "GET" || url.origin !== self.location.origin) {
    return;
  }

  if (!url.pathname.startsWith("/__mockup/")) {
    return;
  }

  event.respondWith((async () => {
    const cache = await caches.open(CACHE_NAME);

    if (request.mode === "navigate") {
      try {
        const networkResponse = await fetch(request);
        if (networkResponse.ok) {
          await cache.put(request, networkResponse.clone());
        }
        return networkResponse;
      } catch {
        return (await cache.match(request)) || (await cache.match("/__mockup/"));
      }
    }

    const cached = await cache.match(request);
    if (cached) {
      return cached;
    }

    try {
      const networkResponse = await fetch(request);
      if (networkResponse.ok) {
        await cache.put(request, networkResponse.clone());
      }
      return networkResponse;
    } catch {
      return new Response("", { status: 503, statusText: "Offline" });
    }
  })());
});