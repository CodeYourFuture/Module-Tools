#!/usr/bin/env node

import { program } from "commander";
import process from "node:process";
import { promises as fs } from "node:fs";

program
  .name("cwc")
  .description("Displays number of lines, words, and bytes in a file")
  .option("-l, --lines", "Counts number of newline characters")
  .option(
    "-w, --words",
    "Counts sequence of characters separated by whitespace",
  )
  .option("-c, --bytes", "Counts raw size of the files in bytes")
  .argument("<files...>", "File(s) to read and count");

program.parse();

const options = program.opts();
const files = program.args;

const noFlags = !options.lines && !options.words && !options.bytes;

let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

async function countFiles(file) {
  try {
    const buffer = await fs.readFile(file);
    const content = buffer.toString("utf-8");

    const lineCount = content === "" ? 0 : content.split("\n").length - 1;
    const wordCount = content.trim() ? content.trim().split(/\s+/).length : 0;
    const byteCount = buffer.length;

    totalLines += lineCount;
    totalWords += wordCount;
    totalBytes += byteCount;

    let result = "";

    if (options.lines || noFlags) result += `${String(lineCount).padStart(8)}`;
    if (options.words || noFlags) result += `${String(wordCount).padStart(8)}`;
    if (options.bytes || noFlags) result += `${String(byteCount).padStart(8)}`;

    process.stdout.write(`${result} ${file}\n`);
  } catch (error) {
    console.error(`cwc: ${file}: ${error.message}`);
    process.exit(1);
  }
}

(async () => {
  for (const file of files) {
    await countFiles(file);
  }

  if (files.length > 1) {
    let total = "";

    if (options.lines || noFlags) total += `${String(totalLines).padStart(8)}`;
    if (options.words || noFlags) total += `${String(totalWords).padStart(8)}`;
    if (options.bytes || noFlags) total += `${String(totalBytes).padStart(8)}`;

    process.stdout.write(`${total} total\n`);
  }
})();
