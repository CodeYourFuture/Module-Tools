import { program } from "commander";
import process from "node:process";
import { promises as fs } from "node:fs";

program
    .name("cat")
    .description("print the content of file")
    .argument("<path>", "The file path to process");
program.parse();

const argv = program.args;
if (argv.length != 1) {
    console.error(`Expected exactly 1 argument (a path) to be passed but got ${argv.length}.`);
    process.exit(1);
}
const path = argv[0];
const content = await fs.readFile(path, "utf-8");
process.stdout.write(content);