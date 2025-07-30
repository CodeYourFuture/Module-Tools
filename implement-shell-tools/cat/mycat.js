import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("mycat")
  .description("Outputs the content of the given file(s), like the cat command")
  .argument("<path>", "The file path to read");

program.parse();

const argv = program.args;
if (argv.length !== 1) {
  console.error(
    `Expected exactly 1 argument (a path) to be passed but got ${argv.length}.`
  );
  process.exit(1);
}

const path = argv[0];
const content = await fs.readFile(path, "utf-8");
process.stdout.write(content);
