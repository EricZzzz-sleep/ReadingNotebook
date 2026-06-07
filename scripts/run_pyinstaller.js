const { spawnSync } = require("node:child_process");
const fs = require("node:fs");
const path = require("node:path");

const root = path.resolve(__dirname, "..");
const localPython = process.platform === "win32"
  ? path.join(root, ".venv", "Scripts", "python.exe")
  : path.join(root, ".venv", "bin", "python");

const candidates = [
  localPython,
  "python",
  "python3",
];

const args = [
  "-m",
  "PyInstaller",
  "--clean",
  "--noconfirm",
  "desktop/quotebook-backend.spec",
  "--distpath",
  "desktop/backend-dist",
  "--workpath",
  "desktop/backend-build",
];

for (const candidate of candidates) {
  if (candidate.includes(path.sep) && !fs.existsSync(candidate)) continue;

  const result = spawnSync(candidate, args, {
    cwd: root,
    stdio: "inherit",
    shell: false,
  });

  if (result.status === 0) process.exit(0);
  if (result.error?.code === "ENOENT") continue;
  process.exit(result.status || 1);
}

console.error("Could not find Python to run PyInstaller.");
process.exit(1);
