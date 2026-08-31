import process from "node:process";
import { promises as fs } from "node:fs";
import { program } from "commander";

program
  .name("Word Count")
  .description("my implementation of wc")
  .argument("<path...>", "The file path to process")
  .option("-l", "Count for the total number of lines")
  .option("-c", "Count the total number of bytes")
  .option("-w", "Count the total number of words");

program.parse();

let filePaths = program.args;
let options = program.opts();
let noFlags = !options.l && !options.w && !options.c;

let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

for (const filePath of filePaths) {
  try {
    const content = await fs.readFile(filePath, "utf-8");
    const outputs = [];

    const lines = getLineCount(content);
    const words = getWordCount(content);
    const bytes = getByteCount(content);

    totalLines += lines;
    totalWords += words;
    totalBytes += bytes;

    if (noFlags || options.l) {
      outputs.push(lines);
    }
    if (noFlags || options.w) {
      outputs.push(words);
    }
    if (noFlags || options.c) {
      outputs.push(bytes);
    }

    outputs.push(filePath);
    console.log(outputs.join("\t"));
  } catch (err) {
    console.error(`${err.message}`);
  }
}

if (filePaths.length > 1) {
  const totalOutputs = [];

  if (noFlags || options.l) {
    totalOutputs.push(totalLines);
  }
  if (noFlags || options.w) {
    totalOutputs.push(totalWords);
  }
  if (noFlags || options.c) {
    totalOutputs.push(totalBytes);
  }
  totalOutputs.push("total");
  console.log(totalOutputs.join("\t"));
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
