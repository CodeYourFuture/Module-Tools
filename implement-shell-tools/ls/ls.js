import { promises as fs } from "node:fs";
import process from "node:process";

const args = process.argv.slice(2);

const showHidden = args.includes("-a");

const supportedFlags = ["-1", "-a"];
const unknownFlags = args.filter(
  (arg) => arg.startsWith("-") && !supportedFlags.includes(arg),
);

if (unknownFlags.length > 0) {
  console.error(`ls: invalid option -- '${unknownFlags[0].slice(1)}'`);
  process.exit(1);
}

const paths = args.filter((arg) => !arg.startsWith("-"));

const targetPaths = paths.length > 0 ? paths : [process.cwd()];

for (const targetPath of targetPaths) {
  if (targetPaths.length > 1) {
    process.stdout.write(`${targetPath}:\n`);
  }

  let entries;

  try {
    entries = await fs.readdir(targetPath);
  } catch (error) {
    console.error(
      `ls: cannot access '${targetPath}': No such file or directory`,
    );
    continue;
  }

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

  if (targetPaths.length > 1) {
    process.stdout.write("\n");
  }
}
