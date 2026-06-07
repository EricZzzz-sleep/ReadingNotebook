const fs = require("node:fs");
const path = require("node:path");

const required = [
  "MAC_CERTIFICATE",
  "MAC_CERTIFICATE_PASSWORD",
  "APPLE_ID",
  "APPLE_APP_SPECIFIC_PASSWORD",
  "APPLE_TEAM_ID",
];

const enabled = required.every((name) => Boolean(process.env[name]));
if (!enabled) {
  console.log("Notarization is disabled because Apple signing secrets are incomplete.");
  process.exit(0);
}

const packagePath = path.resolve(__dirname, "..", "package.json");
const packageJson = JSON.parse(fs.readFileSync(packagePath, "utf8"));
packageJson.build = packageJson.build || {};
packageJson.build.afterSign = "scripts/notarize_mac_app.js";
fs.writeFileSync(packagePath, `${JSON.stringify(packageJson, null, 2)}\n`);
console.log("Notarization enabled for this build.");
