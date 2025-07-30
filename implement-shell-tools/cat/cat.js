import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("my-cat")
  .description("Reimplementation of the Unix `cat` command with -n and -b support")
  .option("-n", "number all lines")
  .option("-b", "number non-empty lines")
  .argument("<files...>", "files to read");

program.parse();

const options = program.opts();
const filePaths = program.args;

let lineNumber = 1;

for (const filePath of filePaths) {
  const content = await fs.readFile(filePath, "utf-8");

  for (const line of content.split("\n")) {
    if (options.n) {
      console.log(`${lineNumber}  ${line}`);
      lineNumber++;
    } else if (options.b) {
      if (line.trim()) {
        console.log(`${lineNumber}  ${line}`);
        lineNumber++;
      } else {
        console.log("");
      }
    } else {
      console.log(line);
    }
  }
}
