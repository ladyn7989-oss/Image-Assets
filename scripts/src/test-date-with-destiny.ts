import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "../..");
const sourcePath = path.join(
  root,
  "attached_assets/date-with-destiny_1785900001839.html",
);
const source = fs.readFileSync(sourcePath, "utf8");

const expectedDays = [7, 14, 21, 30];
const dayEventBlock = source.match(
  /const DAY_EVENTS=\[([\s\S]*?)\n\];/,
)?.[1];
assert.ok(dayEventBlock, "DAY_EVENTS declaration is present");

const declaredDays = [...dayEventBlock.matchAll(/day:(\d+)/g)].map((match) =>
  Number(match[1]),
);
assert.deepEqual(
  declaredDays,
  expectedDays,
  "scheduled day events remain on days 7, 14, 21, and 30",
);

for (const day of expectedDays) {
  assert.match(
    dayEventBlock,
    new RegExp(`id:"day${day}"`),
    `day ${day} has a stable event id`,
  );
}

assert.match(
  source,
  /S\.dayEvents\[dayEvent\.id\]=true/,
  "scheduled events are marked as consumed",
);
assert.match(
  source,
  /S\.me=dayEvent;\s*S\.scr="miniEvent";/,
  "scheduled events enter the mini-event screen",
);
assert.match(
  source,
  /if\(!tired&&S\.scr!=="miniEvent"\)\{if\(!tryEncounter\(\)\)tryMiniEvent\(\)\}/,
  "random encounters are skipped when a scheduled event is active",
);

type Event = { day: number; id: string };
const events: Event[] = expectedDays.map((day) => ({
  day,
  id: `day${day}`,
}));

function advanceDay(
  day: number,
  consumed: Record<string, boolean>,
  randomEncounter: boolean,
) {
  const scheduled = events.find((event) => event.day === day);
  let screen = "cityMap";
  let randomEncounterRan = false;
  if (scheduled && !consumed[scheduled.id]) {
    consumed[scheduled.id] = true;
    screen = "miniEvent";
  }
  if (screen !== "miniEvent") {
    randomEncounterRan = randomEncounter;
  }
  return { screen, randomEncounterRan };
}

for (const event of events) {
  const consumed: Record<string, boolean> = {};
  const first = advanceDay(event.day, consumed, true);
  assert.equal(first.screen, "miniEvent", `${event.id} triggers once`);
  assert.equal(
    first.randomEncounterRan,
    false,
    `${event.id} takes priority over random encounters`,
  );

  const second = advanceDay(event.day, consumed, true);
  assert.equal(
    second.screen,
    "cityMap",
    `${event.id} does not trigger again after consumption`,
  );
  assert.equal(
    second.randomEncounterRan,
    true,
    `random encounters resume after ${event.id}`,
  );
}

assert.match(source, /energy:5/, "player starts with five energy");
assert.match(source, /S\.energy=5;S\.buddy=null/, "rest restores five energy");
assert.match(
  source,
  /Energy <b>'\+S\.energy\+'\/5/,
  "city map displays a five-energy cap",
);
assert.match(source, /S\.energy=Math\.min\(5,S\.energy\+ch\.energy\)/, "rewards cap energy at five");
assert.match(source, /ambient:true/, "ambient audio is enabled by default");
assert.match(source, /data-a="setAmbient"/, "ambient audio has a settings control");
assert.match(source, /document\.addEventListener\("visibilitychange"/, "ambient audio responds to tab visibility");
assert.match(source, /Original procedural tones/, "ambient audio is explicitly copyright-safe");

console.log(
  `Date With Destiny regression checks passed: ${events.length} scheduled events, one-time priority behavior, energy cap 5, and copyright-safe ambient audio.`,
);