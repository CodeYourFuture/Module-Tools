
const { promises: fs } = require("fs");// it reads the files 
const process = require("process");// gets large files information 
const { program } = require("commander");// it puts out in chunks or parses information 

program
  .name("cat")
  .description("A simple implementation of the Unix cat command")
  .option("-n, --number", "Number all output lines")
  .option("-b, --number-nonempty", "Number only non-empty lines")
  .argument("<files...>", "Files to read")
  .parse(process.argv);

const { number: nFlag, numberNonempty: bFlag } = program.opts();
const files = program.args;

let lineNum = 1; // Counting for -n flag
let nonEmptyLineNum = 1; // Counting for -b flag

// Function to print lines with flags
function printLines(lines) {
  lines.forEach((line) => {
    if (bFlag && line.trim()) {
      console.log(`${nonEmptyLineNum++} ${line}`);
    } else if (nFlag) {
      console.log(`${lineNum++} ${line}`);
    } else {
      console.log(line);
    }
  });
}

// Function to read and print file content
async function readFile(file) {
  try {
    const content = await fs.readFile(file, "utf8");
    const lines = content.split("\n");
    printLines(lines);
  } catch (err) {
    console.error(`cat: ${file}: No such file or folder`);
  }
}

// Processing  multiple files
files.forEach(readFile);
