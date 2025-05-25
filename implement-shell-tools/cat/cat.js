const { promises: fs } = require("fs");
const process = require("process");
const { program } = require("commander");

program
  .name("cat")
  .description("Implement a version of the cat program")
  .option("-n, --number", "Number the output lines, starting at 1")
  .option("-b, --number2", "Number the nonempty lines, starting at 1")
  .argument("<paths...>", "The file paths to process")
  .parse(process.argv);

let args = program.args;

const { number: nOption, number2: bOption } = program.opts();
let lineNumber = 1;
let nonEmptyLineNumber = 1;

function printLinesWithOptions(lines) {
  lines.forEach((line, index) => {
    if (nOption) {
      console.log(`${lineNumber++} ${line}`);
    } else if (bOption && line.trim()) {
      console.log(`${nonEmptyLineNumber++} ${line}`);
    } else {
      console.log(line);
    }
  });
}

async function readFileContent(path) {
  try {
    const content = await fs.readFile(path, { encoding: "utf-8" });
    const lines = content.split("\n");
    if(lines[lines.length - 1] === "") {
      lines.pop();
    }
    printLinesWithOptions(lines);
  } catch (err) {
    console.error(`Error reading file ${path}: ${err.message}`);
  }
}

args.forEach((arg) => {
  readFileContent(arg);
});
