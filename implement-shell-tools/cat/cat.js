import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("cat command")
  .description("create cat command")
  .option("-n", "Number all lines")
  .option("-b", "Number non-empty lines")
  .argument("<paths...>", "File paths");

program.parse();
const paths = program.args;
const number = program.opts().n;
const nonEmptyLine = program.opts().b;

let lineNumber = 1;

for (const path of paths) {
  try {
    const read = await fs.readFile(path, "utf-8");
    const lines = read.split("\n");

    function printNumLine(line) {
      console.log(`${String(lineNumber).padStart(6, " ")} ${line}`);
      lineNumber++;
    }

    for (let i of lines) {
      if (number || (nonEmptyLine && i.trim() !== "")) {
        printNumLine(i);
      } else {
        console.log(i);
      }
    }
  } catch (err) {
    console.error(`File could not read: ${path}`);
  }
}
