import { promises as fs } from "node:fs";
import process from "node:process";

const args = process.argv.slice(2);

if (args.length === 0) {
  console.error("Usage: node cat.js [-n] [-b] <file...>");
  process.exit(1);
}
const showAllLineNumbers = args.includes("-n");
const showNonBlankNumbers = args.includes("-b");

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

      let isLastLine;
      if (i === lines.length - 1) {
        isLastLine = true;
      } else {
        isLastLine = false;
      }

      if (isLastLine && line === "") {
        break;
      }

      if (showAllLineNumbers) {
        const paddedNumber = String(lineNumber).padStart(6, " ");
        process.stdout.write(`${paddedNumber}\t${line}\n`);
        lineNumber++;
      } else if (showNonBlankNumbers) {
        if (line.trim() === "") {
          process.stdout.write("\n");
        } else {
          const paddedNumber = String(lineNumber).padStart(6, " ");
          process.stdout.write(`${paddedNumber}\t${line}\n`);
          lineNumber++;
        }
      }
    }
  }
}
