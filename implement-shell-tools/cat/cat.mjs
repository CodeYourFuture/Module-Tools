import { program } from "commander";
import { promises as fs } from "node:fs";

program.name("cat");
program.description("simple cat clone");
program.option("-n, --number", "number all output lines");
program.option("-b, --number-nonblank", "number non-empty output lines");
program.argument("[paths...]", "file(s) to process");
program.parse();

const { number, numberNonblank } = program.opts();
const paths = program.args;

async function processFile(path) {
  try {
    const stat = await fs.stat(path);

    if (stat.isDirectory()) {
      console.error(`${path}: Is a directory`);
      return;
    }

    const content = await fs.readFile(path, { encoding: "utf-8" });
    const lines = content.split("\n");
    const hasTrailingNewLine = content.endsWith("\n");
    const effectiveLines = hasTrailingNewLine ? lines.slice(0, -1) : lines;
    let lineNumber = 1;

    const processed = effectiveLines.map((line) => {
      if (numberNonblank) {
        if (line.trim() !== "") {
          const result = `${lineNumber}\t${line}`;
          lineNumber += 1;
          return result;
        }

        return line;
      }

      if (number) {
        const result = `${lineNumber}\t${line}`;
        lineNumber += 1;
        return result;
      }

      return line;
    });

    const output = processed.join("\n");
    console.log(output);
  } catch (error) {
    console.error(`${path}: ${error.message}`);
  }
}

try {
  for (const path of paths) {
    await processFile(path);
  }
} catch (error) {
  console.error(error.message);
}
