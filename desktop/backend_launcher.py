#!/usr/bin/env python3
"""Run the QuoteBook Django backend for the desktop app."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "backend"
FRONTEND = ROOT / "frontend"


def bundled_root() -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return ROOT


def configure_paths() -> None:
    root = bundled_root()
    backend = root / "backend" if (root / "backend").exists() else BACKEND
    frontend = root / "frontend" if (root / "frontend").exists() else FRONTEND

    sys.path.insert(0, str(backend))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reading_tracker.settings")
    os.environ.setdefault("QUOTEBOOK_FRONTEND_ROOT", str(frontend))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Start the QuoteBook desktop backend.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default="0")
    parser.add_argument("--data-dir", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    os.environ["QUOTEBOOK_DATA_DIR"] = str(Path(args.data_dir).expanduser().resolve())
    configure_paths()

    import django
    from django.core.management import call_command, execute_from_command_line

    django.setup()
    call_command("migrate", interactive=False, verbosity=0)
    execute_from_command_line([
        "quotebook-backend",
        "runserver",
        f"{args.host}:{args.port}",
        "--noreload",
    ])


if __name__ == "__main__":
    main()
