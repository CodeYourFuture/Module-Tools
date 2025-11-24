import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";
import { stat } from "node:fs/promises";

program
  .name("count-containing-lines-words-characters")
  .description("Counts lines, words or characters in a file (or all files) inside a directory")
  .option("-l, --line", "The number of lines in each file")
  .argument("<path>", "The file path to process");

program.parse();

const argv = program.args;

if (argv.length != 1) {
  console.error(
    `Expected exactly 1 argument (a path) to be passed but got ${argv.length}.`
  );
  process.exit(1);
}

const path = argv[0];

const options = program.opts();

const content = await fs.readdir(path);

const pathInfo = await stat(path);

function counter(item) {
  const lines = item.split("\n");
  const words = item.split(/\s+/).filter(Boolean).length;
  const characters = item.length;
  return { lines, words, characters };
}

if (pathInfo.isFile()) {
    const content = await fs.readFile(path, "utf-8");
    const stats = counter(content);
} else if (pathInfo.isDirectory()) {
    const files = await fs.readdir(path);
    for (const file of files) {
        const filePath = `${path}/${file}`;
        const fileContent = await fs.readFile(filePath, "utf-8");
    }
}

