import process from "node:process";
import { promises as fs } from "node:fs";

let filePaths = [];
let flag = null;
let numberOfWords;

if (process.argv[2].startsWith("-")) {
  flag = process.argv[2];
  filePaths = process.argv.slice(3);
} else {
  filePaths = process.argv.slice(2);
}
for (const filePath of filePaths) {
  const content = await fs.readFile(filePath, "utf-8");

  if (flag === "-w") {
    console.log(getWordCount(content));
  } else if (flag === "-l") {
    console.log(getLineCount(content));
  } else if (flag === "-c") {
    console.log(getByteCount(content), filePaths);
  } else {
    console.log(
      getWordCount(content),
      getLineCount(content),
      getByteCount(content),
      filePaths,
    );
  }
}

function getWordCount(text) {
  const trimmed = text.trim();
  if (trimmed.length == 0) {
    return 0;
  }
  return trimmed.split(/\s+/).length;
}

function getLineCount(text) {
  if (text.length == 0) return 0;
  return text.split("\n").length - 1;
}

function getByteCount(text) {
  return Buffer.byteLength(text, "utf-8");
}
