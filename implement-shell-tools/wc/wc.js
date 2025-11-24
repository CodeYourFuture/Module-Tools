import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("node-cat")
  .description("A Node.js implementation of the Unix cat command")
  .option("-n, --number", "Number all output lines")
  .option(
    "-b, --numberNonBlank",
    "Numbers only non-empty lines. Overrides -n option"
  )
  .argument("<path...>", "The file path to process");

program.parse();

const paths = program.args;
const { number, numberNonBlank } = program.opts();

// --- Read files and sizes ---
let content = "";
let fileSize;

for (const path of paths) {
  content = await fs.readFile(path, "utf-8");
  if (content.endsWith("\n")) {
    content = content.slice(0, -1);
  }
  fileSize = await fs.stat(path);
  console.log(
    getLineCount(content),
    getWordCount(content),
    fileSize.size,
    path
  );
}

function getWordCount(text) {
  let words, lines;

  lines = text.split("\n");
  // console.log(lines);
  words = lines.flatMap((line) => line.split(" "));

  return words.filter((word) => word.length > 0).length;
}

function getLineCount(text) {
  let lines;
  return (lines = text.split("\n").length);
}

// 1   4  20 sample-files/1.txt
// 1   7  39 sample-files/2.txt
// 5  24 125 sample-files/3.txt
// 7  35 184 total
