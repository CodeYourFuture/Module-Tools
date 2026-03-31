import { promises as fs } from "node:fs";
import { program } from "commander";
import { dirxml } from "node:console";

program
  .name("ls ")
  .description("ls implementation")
  .argument("[path]", "The path to process")
  .option("-1, --one-per-line", "one file per line")
  .option("-a", "show hidden files");
program.parse();

const path = program.args[0] || ".";
const options = program.opts();
try {
  const files = await fs.readdir(path);
  if (options.onePerLine && options.a) {
    for (const file of files) {
      console.log(file);
    }
  } else if (options.onePerLine) {
    for (const file of files) {
      if (!file.startsWith(".")) {
        console.log(file);
      }
    }
  } else if (options.a) {
    for (const file of files) {
      process.stdout.write(file + " ");
    }
  } else {
    for (const file of files) {
      if (!file.startsWith(".")) {
        process.stdout.write(file + " ");
      }
    }
  }
} catch (error) {
  console.error(error.message);
}
