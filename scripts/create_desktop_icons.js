const fs = require("node:fs");
const path = require("node:path");

const root = path.resolve(__dirname, "..");
const source = path.join(root, "frontend", "assets", "app-icon-512.png");
const build = path.join(root, "desktop", "build");

function uint32BE(value) {
  const buffer = Buffer.alloc(4);
  buffer.writeUInt32BE(value);
  return buffer;
}

function uint16LE(value) {
  const buffer = Buffer.alloc(2);
  buffer.writeUInt16LE(value);
  return buffer;
}

function uint32LE(value) {
  const buffer = Buffer.alloc(4);
  buffer.writeUInt32LE(value);
  return buffer;
}

function createIcns(png) {
  const icon = Buffer.concat([Buffer.from("ic09"), uint32BE(png.length + 8), png]);
  return Buffer.concat([Buffer.from("icns"), uint32BE(icon.length + 8), icon]);
}

function createIco(png) {
  const header = Buffer.concat([uint16LE(0), uint16LE(1), uint16LE(1)]);
  const directory = Buffer.concat([
    Buffer.from([0, 0, 0, 0]),
    uint16LE(1),
    uint16LE(32),
    uint32LE(png.length),
    uint32LE(22),
  ]);
  return Buffer.concat([header, directory, png]);
}

fs.mkdirSync(build, { recursive: true });
const png = fs.readFileSync(source);
fs.writeFileSync(path.join(build, "icon.icns"), createIcns(png));
fs.writeFileSync(path.join(build, "icon.ico"), createIco(png));
