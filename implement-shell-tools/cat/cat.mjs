import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("implement my own version of `cat`.")
  .description("I do not know what I'm doing")
  .argument("<path>", "The file path to process");
program.parse();

const argv = program.args;
if (argv.length != 1) {
console.error(`Expected exactly 1 argument (a path) to  be passed but got ${argv.length}`);
process.exit(1);
}
const path = argv[0];

const content = await fs.readFile(path, "utf-8");
console.log(content);