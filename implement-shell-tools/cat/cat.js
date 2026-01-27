import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("display-file-content")
  .description("Implement cat command with -n and -b flag support")
  .option("-n, --number-all-lines", "Number every line in the file")
  .option("-b, --number-non-empty-lines", "Number non empty lines in the file")
  .argument("<paths...>", "File paths to process");

program.parse(process.argv);

const args = program.args; //Array all file paths

//read flags user typed and return them as object.
const opts = program.opts();

let lineNumber = 1;

// Loop over every filepath in args
args.forEach(async (filepath) => {
  const content = await fs.readFile(filepath, "utf8");
  const lines = content.split("\n");

  lines.forEach((line) => {
    if (opts.numberAllLines) {
      // -n: number every line
      console.log(`${lineNumber} ${line}`);
      lineNumber++;
    } else if (opts.numberNonEmptyLines) {
      // -b: number non-empty lines only
      if (line.trim() === "") {
        console.log(line);
      } else {
        console.log(`${lineNumber} ${line}`);
        lineNumber++;
      }
    } else {
      // No flag: just print
      console.log(line);
    }
  });
});
