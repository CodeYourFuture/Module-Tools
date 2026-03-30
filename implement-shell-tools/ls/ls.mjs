import { promises as fs } from "node:fs";
import { program } from "commander";

program
  .name("ls implementation")
  .description("ls -1 program")
  .argument("[path]", "The path to process")
  .option("-1, --one-per-line", "one file per line");
program.parse();

const path = program.args[0] || ".";
const options = program.opts();
try {
  const files = await fs.readdir(path);
  
  if (options.onePerLine) {
    for (const file of files) {
      if (!file.startsWith(".")) {
        console.log(file);
      }
    }
  }
} catch (error) {
  console.error(error.message);
}
