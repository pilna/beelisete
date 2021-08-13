from os import getenv

WIDTH = int(getenv("WIDTH", "1920"))
HEIGHT = int(getenv("HEIGHT", "1080"))

TILE_WIDTH = int(getenv("TILE_WIDTH", "32"))
TILE_HEIGHT = int(getenv("TILE_HEIGHT", "32"))