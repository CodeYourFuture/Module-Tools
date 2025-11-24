import { program } from "commander";
import { on } from "node:events";
import { promises as fs } from "node:fs";
import path from "node:path";

program
  .name("node-ls")
  .description("A Node.js implementation of the Unix ls command")
  .option("-1", "list one file per line")
  .option(
    "-a, --all",
    "include directory entries whose names begin with a dot (.)"
  )
  .argument("[directory]", "The file path to process");
program.parse();

const paths = program.args;
const { 1: onePerLine, all } = program.opts();

const directory = paths.length === 0 ? "." : paths[0];

let entries = await fs.readdir(directory);

if (onePerLine) {
  console.log(entries.filter((entry) => entry[0] !== ".").join("\n"));
  // entries.filter((entry) => { entry[0] === "." })
}

