#!/usr/bin/env python3
"""Create desktop installer icons from the QuoteBook PNG icon."""

from __future__ import annotations

import struct
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "frontend" / "assets" / "app-icon-512.png"
BUILD = ROOT / "desktop" / "build"


def create_icns(png_bytes: bytes) -> bytes:
    icon_type = b"ic09"
    icon = icon_type + struct.pack(">I", len(png_bytes) + 8) + png_bytes
    return b"icns" + struct.pack(">I", len(icon) + 8) + icon


def create_ico(png_bytes: bytes) -> bytes:
    header = struct.pack("<HHH", 0, 1, 1)
    directory = struct.pack("<BBBBHHII", 0, 0, 0, 0, 1, 32, len(png_bytes), 22)
    return header + directory + png_bytes


def main() -> None:
    BUILD.mkdir(parents=True, exist_ok=True)
    png_bytes = SOURCE.read_bytes()
    (BUILD / "icon.icns").write_bytes(create_icns(png_bytes))
    (BUILD / "icon.ico").write_bytes(create_ico(png_bytes))


if __name__ == "__main__":
    main()
