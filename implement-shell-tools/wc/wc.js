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

const paths = program.args;
const { lines, words, bytes } = program.opts();

const showAll = !lines && !words && !bytes;

// --- Read files and sizes ---
let content = "";
let output = [];

let lineCountTotal = 0,
  wordCountTotal = 0,
  fileSizeTotal = 0;

if (Object.keys(program.opts()).length === 1) {
}

for (const path of paths) {
  let fileStats;
  let data = {};

  content = await fs.readFile(path, "utf-8");
  if (content.endsWith("\n")) {
    content = content.slice(0, -1);
  }

  data.lineCount = getLineCount(content);
  lineCountTotal += data.lineCount;

  data.wordCount = getWordCount(content);
  wordCountTotal += data.wordCount;

  fileStats = await fs.stat(path);
  data.fileSize = fileStats.size;
  fileSizeTotal += data.fileSize;

  data.path = path;
  output.push(data);
}

console.log(output);

if (paths.length > 1) {
  console.log(
    `${String(lineCountTotal).padStart(3)}${String(wordCountTotal).padStart(
      4
    )}${String(fileSizeTotal).padStart(4)} total`
  );
}

// output.push(String(fileSize.size).padStart(4));
// console.log(`${output.join("")} ${path}`);

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
