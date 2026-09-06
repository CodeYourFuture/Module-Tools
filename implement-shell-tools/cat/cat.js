import { promises as fs } from "node:fs";
import process from "node:process";

const args = process.argv.slice(2);

if (args.length === 0) {
  console.error("Usage: node cat.js [-n] [-b] <file...>");
  process.exit(1);
}
const showAllLineNumbers = args.includes("-n");
const showNonBlankNumbers = args.includes("-b");
const supportedFlags = ["-n", "-b"];
const unknownFlags = args.filter(
  (arg) => arg.startsWith("-") && !supportedFlags.includes(arg),
);

if (unknownFlags.length > 0) {
  console.error(`cat: invalid option -- '${unknownFlags[0].slice(1)}'`);
  process.exit(1);
}

const filePaths = args.filter((arg) => !arg.startsWith("-"));

let lineNumber = 1;

for (const filePath of filePaths) {
  const content = await fs.readFile(filePath, "utf-8");

  if (!showAllLineNumbers && !showNonBlankNumbers) {
    process.stdout.write(content);
  } else {
    const lines = content.split("\n");

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];

      const isLastLine = i === lines.length - 1;

      if (isLastLine && line === "") {
        break;
      }

      const isBlankLine = line.trim() === "";
      const needsLineNumber =
        showAllLineNumbers || (showNonBlankNumbers && !isBlankLine);

      if (needsLineNumber) {
        const paddedNumber = String(lineNumber).padStart(6, " ");
        process.stdout.write(`${paddedNumber}\t${line}\n`);
        lineNumber++;
      } else if (showNonBlankNumbers && isBlankLine) {
        process.stdout.write("\n");
      }
    }
  }
}
