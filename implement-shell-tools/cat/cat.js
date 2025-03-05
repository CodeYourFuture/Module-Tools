import { promises as fs, read } from "node:fs";
import process from "node:process";
import { program } from "commander";

program
  .name("Implement cat")
  .description("Implement a version of the cat program")
  .option("-n, --number", "Number the output lines, starting at 1")
  .option("-b, --number2", "Number the nonempty lines, starting at 1")
  .argument("<paths...>", "The file paths to process")
  .parse(process.argv);

let args = program.args;

const numberLines = program.opts().number;
const numberLines2 = program.opts().number2;
let lineNumber = 1;

async function printFileWithLineNumbers(path) {
  try {
    const content = await fs.readFile(path, { encoding: "utf-8" });
    const lines = extractLinesFromContent(content);
    lines.forEach((line) => {
      if (numberLines) {
        console.log(`${lineNumber++} ${line}`);
        return;
      }

      if (numberLines2) {
        if (line !== "") {
          console.log(`${lineNumber++} ${line}`);
          return;
        }
      }

      console.log(line);
    });
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

// display file/s contents with line numbers.
await Promise.all(args.map(printFileWithLineNumbers));
