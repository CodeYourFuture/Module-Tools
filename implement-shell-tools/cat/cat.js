import { promises as fs } from "node:fs";
import process from "node:process";
import { program } from "commander";

program
  .name("Implement cat")
  .description("Implement a version of the cat program")
  .option("-n, --number", "Number the output lines, starting at 1")
  .option("-b, --number2", "Number the nonempty lines, starting at 1")
  .argument("<paths...>", "The file paths to process")
  .parse(process.argv);

const args = program.args;

const displayLineNumber = program.opts().number;
const bOption = program.opts().number2;
let lineNumber = 1;

async function readAndPrintFileContent(path) {
  try {
    const content = await fs.readFile(path, { encoding: "utf-8" });
    const lines = extractLinesFromContent(content);
    printLinesWithOptions(lines);
  } catch (err) {
    console.error(err.message);
  }
}

function extractLinesFromContent(content) {
  const lines = content.split("\n");
  if (lines[lines.length - 1] === "") {
    lines.pop(); // excludes last line if empty
  }
  return lines;
}

function printLinesWithOptions(lines) {
  lines.forEach((line) => {
    if (displayLineNumber) {
      console.log(`${lineNumber++} ${line}`);
      return;
    }

    if (bOption) {
      if (line !== "") {
        console.log(`${lineNumber++} ${line}`);
        return;
      }
    }

    console.log(line);
  });
}
// display file/s contents with line numbers.
await Promise.all(args.map(readAndPrintFileContent));
