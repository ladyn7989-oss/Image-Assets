#!/usr/bin/env python3
"""Download all character sprite assets from GitHub for the Ren'Py build."""
import os
import urllib.request
import json

BASE_URL = "https://raw.githubusercontent.com/ladyn7989-oss/Image-Assets/main"
DEST = "game/images/characters"

os.makedirs(DEST, exist_ok=True)

# Character sprite mapping - download all sprites to local images folder
sprite_map = {
    "aether": ["angry", "belly", "blush", "gentle-laugh", "happy", "looking-away", "neutral", "serious", "shy", "soft-smile", "surprised"],
    "fomo": ["angry", "belly", "blush", "happy", "sad", "smug", "surprised"],
    "glacia": ["angry", "blush", "ending", "happy", "portrait", "sad", "smug", "surprised"],
    "luce": ["angry", "belly", "blush", "happy", "sad", "smug", "surprised"],
    "luna": ["angry", "belly", "blush", "gentle-laugh", "happy", "looking-away", "neutral", "serious", "shy", "soft-smile", "surprised"],
    "nyx": ["angry", "base", "belly", "blush", "happy", "sad", "smug", "surprised"],
    "riko": ["angry", "base", "blush", "happy", "sad", "smug", "surprised"],
    "wolf": ["angry", "belly", "blush", "gentle-laugh", "happy", "looking-away", "neutral", "serious", "shy", "soft-smile", "surprised"],
    "beerus": ["happy", "angry", "sad", "surprised", "blush", "smug", "ending", "belly", "portrait"],
    "champa": ["happy", "angry", "sad", "surprised", "blush", "smug", "ending", "belly", "portrait"],
    "husk": ["happy", "angry", "sad", "surprised", "blush", "smug", "ending", "belly", "portrait"],
    "vox": ["happy", "angry", "sad", "surprised", "blush", "smug", "ending", "belly", "portrait"],
    "vegeta": ["happy", "angry", "sad", "surprised", "blush", "smug", "ending", "belly", "portrait"],
    "anubis": ["happy", "angry", "sad", "surprised", "blush", "smug", "ending", "belly", "portrait"],
    "vincent": ["happy", "angry", "sad", "surprised", "blush", "smug", "ending", "belly", "portrait"],
    "zero": ["angry", "belly", "blush", "happy", "sad", "smug", "surprised"],
    # Beastars characters (using GitHub beastars/ folder)
    "louis": ["base", "happy", "angry", "sad", "surprised", "blush", "smug", "belly", "ending"],
    "legoshi": ["base", "happy", "angry", "sad", "surprised", "blush", "smug", "belly", "ending"],
    "riz": ["base", "happy", "angry", "sad", "surprised", "blush", "smug", "belly", "ending"],
    "bill": ["base", "happy", "angry", "sad", "surprised", "blush", "smug", "belly", "ending"],
    "gohin": ["base", "happy", "angry", "sad", "surprised", "blush", "smug", "belly", "ending"],
    "solene": ["base", "happy", "angry", "sad", "surprised", "blush", "smug", "belly", "ending"],
}

# Two URL patterns - date-with-destiny folder and beastars folder
def get_url(char, expr):
    if char in ["louis", "legoshi", "riz", "bill", "gohin", "solene"]:
        return f"{BASE_URL}/beastars/{char}-{expr}.png"
    elif char in ["aether", "fomo", "glacia", "luce", "luna", "nyx", "riko", "wolf", "zero"]:
        return f"{BASE_URL}/artifacts/mockup-sandbox/public/images/date-with-destiny/{char}-{expr}.png"
    else:
        return f"{BASE_URL}/artifacts/mockup-sandbox/public/images/date-with-destiny/{char}-{expr}.png"

count = 0
for char, expressions in sprite_map.items():
    for expr in expressions:
        url = get_url(char, expr)
        filename = f"{DEST}/{char}_{expr}.png"
        try:
            urllib.request.urlretrieve(url, filename)
            count += 1
        except Exception as e:
            print(f"SKIP: {char}-{expr} ({e})")

print(f"Downloaded {count} sprites to {DEST}/")
