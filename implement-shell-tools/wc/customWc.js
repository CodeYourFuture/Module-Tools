import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("Custom-wc")
  .description("Custom-wc-that-works-like-wc")
  .argument("<path>", "Path of file to process");

program.parse();

const argumentArray = program.args;
if (argumentArray.length === 0) {
  console.log(`We need at least one file path to process`);
  process.exit(1);
}

const pathArray = argumentArray;

let numberOfLines = 0;

let totalOfLines = 0;

for (let path of pathArray) {
  const file = await fs.readFile(path, "utf-8");
  const lines = file.trimEnd().split("\n");
  numberOfLines = lines.length;
  console.log(lines);
}
