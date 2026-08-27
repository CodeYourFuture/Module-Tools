const fs = require("fs");

const args = process.argv.slice(2);

let countLines = false;
let countWords = false;
let countBytes = false;

let files = [];

for (let arg of args) {
  if (arg === "-l") {
    countLines = true;
  } else if (arg === "-w") {
    countWords = true;
  } else if (arg === "-c") {
    countBytes = true;
  } else {
    files.push(arg);
  }
}

if (!countLines && !countWords && !countBytes) {
  countLines = true;
  countWords = true;
  countBytes = true;
}

let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;
let filesCounted = 0;

function formatResult(lines, words, bytes, fileName) {
  let result = "";
  if (countLines) {
    result += String(lines).padStart(8);
  }
  if (countWords) {
    result += String(words).padStart(8);
  }
  if (countBytes) {
    result += String(bytes).padStart(8);
  }
  return result + " " + fileName;
}

function countFile(fileName) {
  try {
    const content = fs.readFileSync(fileName, "utf8");
    let lines = content.split("\n").length - 1;
    let words = content
      .trim()
      .split(/\s+/)
      .filter((word) => word.length > 0).length;
    let bytes = Buffer.byteLength(content);
    totalLines += lines;
    totalWords += words;
    totalBytes += bytes;
    filesCounted++;
    console.log(formatResult(lines, words, bytes, fileName));
  } catch (error) {
    console.log("Cannot read file: " + fileName);
  }
}

for (let file of files) {
  countFile(file);
}

if (filesCounted > 1) {
  console.log(formatResult(totalLines, totalWords, totalBytes, "total"));
}
