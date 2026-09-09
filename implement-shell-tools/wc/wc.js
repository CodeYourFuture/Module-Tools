import { readFile } from "node:fs/promises";
import process from "node:process";
import { parseArgs } from "node:util";

const { values, positionals: files } = parseArgs({
  args: process.argv.slice(2),

  options: {
    lines: {
      type: "boolean",
      short: "l",
    },

    words: {
      type: "boolean",
      short: "w",
    },

    bytes: {
      type: "boolean",
      short: "c",
    },
  },

  allowPositionals: true,
});

const countLines = values.lines ?? false;
const countWords = values.words ?? false;
const countBytes = values.bytes ?? false;

function printCounts(lines, words, bytes, label) {
  const parts = [];

  if (countLines) {
    parts.push(lines);
  }

  if (countWords) {
    parts.push(words);
  }

  if (countBytes) {
    parts.push(bytes);
  }

  if (!countLines && !countWords && !countBytes) {
    parts.push(lines, words, bytes);
  }

  const output = parts.map((value) => String(value).padStart(8)).join("");

  process.stdout.write(`${output} ${label}\n`);
}

let totalWords = 0;
let totalLines = 0;
let totalBytes = 0;

for (const file of files) {
  try {
    const content = await readFile(file, "utf-8");
    const arrayOfLines = content.split("\n");
    const arrayOfWords = content.trim().split(/\s+/)
    const bytes = Buffer.byteLength(content, "utf-8");
    const lines = arrayOfLines.length -1;
    const words = arrayOfWords.length;
    totalLines += lines;
    totalBytes += bytes;
    totalWords += words;
    printCounts(lines, words, bytes, file);

  } catch (err) {
    console.error(err.message);
  }
}

if (files.length > 1) {
  printCounts(
    totalLines,
    totalWords,
    totalBytes,
    "total"
  );
}