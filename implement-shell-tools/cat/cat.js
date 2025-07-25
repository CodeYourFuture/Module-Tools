import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("my-cat")
  .description("Reads and prints one or more files, optionally numbering lines continuously")
  .argument("<paths...>", "One or more file paths")
  .option("-n, --number", "Number all output lines", false)
  .option("-b, --number-nonblank", "Number non-empty output lines", false);

program.parse();

const filePaths = program.args;
const options = program.opts();

const numberNonBlank = options.numberNonblank;
const numberAll = options.number && !numberNonBlank;

(async () => {
  let lineNumber = 1; // continuous line numbering

  for (const path of filePaths) {
    try {
      const content = await fs.readFile(path, "utf-8");
      const lines = content.split("\n");

      if (numberNonBlank) {
        const maxDigits = String(lines.filter(line => line.trim() !== '').length).length;

        for (const line of lines) {
          if (line.trim() === '') {
            process.stdout.write("\n");
          } else {
            const numStr = String(lineNumber++).padStart(maxDigits, " ");
            process.stdout.write(`${numStr}\t${line}\n`);
          }
        }
      } else if (numberAll) {
        const maxDigits = String(lines.length * filePaths.length).length; // max digits to pad across files

        for (const line of lines) {
          const numStr = String(lineNumber++).padStart(maxDigits, " ");
          process.stdout.write(`${numStr}\t${line}\n`);
        }
      } else {
        // no numbering, just print file content as is
        process.stdout.write(content);
        if (!content.endsWith("\n")) {
          process.stdout.write("\n"); // ensure newline after file if missing
        }
      }
    } catch (err) {
      console.error(`Error reading file "${path}": ${err.message}`);
      process.exit(1);
    }
  }
})();
