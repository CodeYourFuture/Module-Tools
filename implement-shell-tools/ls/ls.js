import { promises as fs } from "node:fs";
import process from "node:process";

const args = process.argv.slice(2);

const showHidden = args.includes("-a");

const paths = args.filter((arg) => !arg.startsWith("-"));

const targetPath = paths.length > 0 ? paths[0] : process.cwd();

let entries = await fs.readdir(targetPath);

if (!showHidden) {
  entries = entries.filter((entry) => !entry.startsWith("."));
}

if (showHidden) {
  entries = [".", "..", ...entries];
}

entries.sort((a, b) => {
  const cleanA = a.replace(/^\.+/, "");
  const cleanB = b.replace(/^\.+/, "");
  return cleanA.localeCompare(cleanB);
});

for (const entry of entries) {
  process.stdout.write(entry + "\n");
}
