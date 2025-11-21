import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("node-cat")
  .description("A Node.js implementation of the Unix cat command")
  .option("-c, --char <char>", "The character to search for", "e")
  .option("-n, --count [type]", "Count type: words or chars")
  .argument("<path...>", "The file path to process");

program.parse();

const argv = program.args;

const path = argv[0];

const content = await fs.readFile(path, "utf-8");

console.log(content.trim());
