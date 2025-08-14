const { promises: fs } = require("fs");
const { program } = require("commander");

program
  .name("cat")
  .description("Implement a version of the cat program")
  .option("-n, --number", "Number all output lines, starting at 1")
  .option("-b, --number2", "Number non-empty output lines, starting at 1")
  .argument("<paths...>", "The file paths to process")
  .parse();

const { number: nOption, number2: bOption } = program.opts();
const paths = program.args;

let lineNumber = 1;
let nonEmptyLineNumber = 1;

function printLinesWithOptions(lines) {
  lines.forEach(line => {
    if (nOption) {
      console.log(`${String(lineNumber++).padStart(6)}  ${line}`);
    } else if (bOption && line.trim()) {
      console.log(`${String(nonEmptyLineNumber++).padStart(6)}  ${line}`);
    } else {
      console.log(line);
    }
  });
}

async function readFileContent(path) {
  try {
    const content = await fs.readFile(path, "utf-8");
    const lines = content.split("\n");
    printLinesWithOptions(lines);
  } catch (err) {
    console.error(`Error reading file ${path}: ${err.message}`);
  }
}

Promise.all(paths.map(readFileContent));
