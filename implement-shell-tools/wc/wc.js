// Power shell commands with Js codes

const fs = require("fs");
const args = process.argv.slice(2);

let flags = [];
let paths = [];

// Check arguments: separate flags and paths
args.forEach((arg) => {
  if (arg.startsWith("-")) {
    flags.push(arg);
  } else {
    paths.push(arg);
  }
});

let totalLines = 0;
let totalWords = 0;
let totalCharacters = 0;

paths.forEach((file) => {
  const content = fs.readFileSync(file, "utf-8");

  const lines = content.split("\n").length - 1;
  const words = content.trim().split(/\s+/).length;
  const chars = content.length;

  if (flags.length === 0) {
    console.log(lines, words, chars, file);
  } else {
    let output = [];

    if (flags.includes("-l")) {
      output.push(lines);
    }

    if (flags.includes("-w")) {
      output.push(words);
    }

    if (flags.includes("-c")) {
      output.push(chars);
    }

    console.log(...output, file);
  }

  totalLines += lines;
  totalWords += words;
  totalCharacters += chars;
});
if (paths.length > 1) {
  let totalOutput = [];

  if (flags.length === 0) {
    totalOutput.push(totalLines, totalWords, totalCharacters);
  } else {
    if (flags.includes("-l")) {
      totalOutput.push(totalLines);
    }

    if (flags.includes("-w")) {
      totalOutput.push(totalWords);
    }

    if (flags.includes("-c")) {
      totalOutput.push(totalCharacters);
    }
  }

  console.log(...totalOutput, "total");
}
