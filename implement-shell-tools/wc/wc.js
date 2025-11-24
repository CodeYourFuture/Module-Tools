import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("node-wc")
  .description("A Node.js implementation of the Unix wc command")
  .option("-l, --lines", "Print the newline counts")
  .option("-w, --words", "Print the word counts")
  .option("-c, --bytes", "Print the byte counts")
  .argument("<path...>", "The file path to process");

program.parse();

const filePaths = program.args;
const { lines, words, bytes } = program.opts();

// When no options are provided, show all counts
const showAll = !lines && !words && !bytes;

// --- Read files and sizes ---
let fileContent = "";
let outputData = [];

let lineCountTotal = 0,
  wordCountTotal = 0,
  fileSizeTotal = 0;

for (const path of filePaths) {
  let fileStats;
  let fileData = {};

  fileContent = await fs.readFile(path, "utf-8");

  fileData.lineCount = getLineCount(fileContent);
  lineCountTotal += fileData.lineCount;

  fileData.wordCount = getWordCount(fileContent);
  wordCountTotal += fileData.wordCount;

  fileStats = await fs.stat(path);
  fileData.fileSize = fileStats.size;
  fileSizeTotal += fileData.fileSize;

  fileData.path = path;
  outputData.push(fileData);
}

console.log(outputData.map(formatOutput).join("\n"));

if (filePaths.length > 1) {
  console.log(
    `${String(lineCountTotal).padStart(3)}${String(wordCountTotal).padStart(
      4
    )}${String(fileSizeTotal).padStart(4)} total`
  );
}

function formatOutput({ lineCount, wordCount, fileSize, path }) {
  let output = [];
  if (lines || showAll) output.push(String(lineCount).padStart(3));
  if (words || showAll) output.push(String(wordCount).padStart(4));
  if (bytes || showAll) output.push(String(fileSize).padStart(4));

  return `${output.join("")} ${path}`;
}

function getWordCount(text) {
  let words, lines;

  lines = text.split("\n");
  words = lines.flatMap((line) => line.split(" "));

  return words.filter((word) => word.length > 0).length;
}

function getLineCount(text) {
  return text.split("\n").length;
}
