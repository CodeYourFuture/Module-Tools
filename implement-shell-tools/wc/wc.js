import { promises as fs } from "node:fs";
import process from "node:process";

const args = process.argv.slice(2);

const showLines = args.includes("-l");
const showWords = args.includes("-w");
const showBytes = args.includes("-c");

const noSpecificFlag = !showLines && !showWords && !showBytes;

const filePaths = args.filter((arg) => !arg.startsWith("-"));

if (filePaths.length === 0) {
  console.error("Usage: node wc.js [-l] [-w] [-c] <file...>");
  process.exit(1);
}

const results = [];

for (const filePath of filePaths) {
  const content = await fs.readFile(filePath, "utf-8");

  const lines = content.endsWith("\n")
    ? content.split("\n").length - 1
    : content.split("\n").length;

  const words = content.split(/\s+/).filter((w) => w.length > 0).length;

  const bytes = Buffer.byteLength(content, "utf-8");

  results.push({ filePath, lines, words, bytes });
}

const totalLines = results.reduce((sum, r) => sum + r.lines, 0);
const totalWords = results.reduce((sum, r) => sum + r.words, 0);
const totalBytes = results.reduce((sum, r) => sum + r.bytes, 0);

let maxNumber;

if (noSpecificFlag) {
  maxNumber = Math.max(totalLines, totalWords, totalBytes);
} else if (showLines) {
  maxNumber = totalLines;
} else if (showWords) {
  maxNumber = totalWords;
} else {
  maxNumber = totalBytes;
}

const width = String(maxNumber).length + 2;

function formatLine(counts, label) {
  const parts = counts.map((n) => String(n).padStart(width, " "));
  return parts.join("") + " " + label;
}

for (const { filePath, lines, words, bytes } of results) {
  if (noSpecificFlag) {
    process.stdout.write(formatLine([lines, words, bytes], filePath) + "\n");
  } else if (showLines) {
    process.stdout.write(formatLine([lines], filePath) + "\n");
  } else if (showWords) {
    process.stdout.write(formatLine([words], filePath) + "\n");
  } else if (showBytes) {
    process.stdout.write(formatLine([bytes], filePath) + "\n");
  }
}

if (results.length > 1) {
  if (noSpecificFlag) {
    process.stdout.write(
      formatLine([totalLines, totalWords, totalBytes], "total") + "\n",
    );
  } else if (showLines) {
    process.stdout.write(formatLine([totalLines], "total") + "\n");
  } else if (showWords) {
    process.stdout.write(formatLine([totalWords], "total") + "\n");
  } else if (showBytes) {
    process.stdout.write(formatLine([totalBytes], "total") + "\n");
  }
}
