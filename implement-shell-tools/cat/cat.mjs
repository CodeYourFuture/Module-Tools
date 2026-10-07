import process from "node:process";
import { promises as fs } from "node:fs";
import { program } from "commander";

program
  .name("Cat")
  .description("My version of cat command line tool")
  .argument("<files...>", "Files to display")
  .option("-n, --number", "Number all output lines")
  .option("-b, --non-blank", "Number non empty output lines");

program.parse();

const { number, nonBlank } = program.opts();
const filePaths = program.args;

let lineNumber = 1;

for (const filePath of filePaths) {
  try {
    const content = await fs.readFile(filePath, "utf-8");

    if (!number && !nonBlank) {
      process.stdout.write(content);
      continue;
    }
    let text = content;
    if (content.endsWith("\n")) {
      text = content.slice(0, -1);
    }
    const lines = text.split("\n");

    for (const line of lines) {
      if (nonBlank) {
        if (line == "") {
          console.log();
        } else {
          console.log(`${lineNumber}\t${line}`);
          lineNumber++;
        }
      } else if (number) {
        console.log(`${lineNumber}\t${line}`);
        lineNumber++;
      }
    }
  } catch (error) {
    console.error(`${error}`);
  }
}
