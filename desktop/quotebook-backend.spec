# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path


ROOT = Path(SPECPATH).parent

block_cipher = None

a = Analysis(
    [str(ROOT / "desktop" / "backend_launcher.py")],
    pathex=[str(ROOT / "backend"), str(ROOT)],
    binaries=[],
    datas=[
        (str(ROOT / "backend" / "books" / "migrations"), "backend/books/migrations"),
        (str(ROOT / "frontend"), "frontend"),
    ],
    hiddenimports=[
        "books",
        "books.admin",
        "books.apps",
        "books.migrations",
        "books.migrations.0001_initial",
        "books.migrations.0002_reading_activity",
        "books.migrations.0003_remove_daily_goal_pages",
        "books.models",
        "books.urls",
        "books.views",
        "reading_tracker",
        "reading_tracker.asgi",
        "reading_tracker.settings",
        "reading_tracker.urls",
        "reading_tracker.wsgi",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.messages",
        "django.contrib.sessions",
        "django.contrib.staticfiles",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="quotebook-backend",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
