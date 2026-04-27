import { promises as fs } from "node:fs";
import process from "node:process";

const args = process.argv.slice(2);

const expandedArgs = [];
for (const arg of args) {
  if (arg.startsWith("-") && arg.length > 2) {
    for (const char of arg.slice(1)) {
      expandedArgs.push(`-${char}`);
    }
  } else {
    expandedArgs.push(arg);
  }
}

const showLines = expandedArgs.includes("-l");
const showWords = expandedArgs.includes("-w");
const showBytes = expandedArgs.includes("-c");

const supportedFlags = ["-l", "-w", "-c"];
const unknownFlags = expandedArgs.filter(
  (arg) => arg.startsWith("-") && !supportedFlags.includes(arg),
);

if (unknownFlags.length > 0) {
  console.error(`wc: invalid option -- '${unknownFlags[0].slice(1)}'`);
  process.exit(1);
}

const noSpecificFlag = !showLines && !showWords && !showBytes;

const filePaths = expandedArgs.filter((arg) => !arg.startsWith("-"));

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

function getCounts(lines, words, bytes) {
  const counts = [];
  if (noSpecificFlag || showLines) counts.push(lines);
  if (noSpecificFlag || showWords) counts.push(words);
  if (noSpecificFlag || showBytes) counts.push(bytes);
  return counts;
}

const maxNumber = Math.max(...getCounts(totalLines, totalWords, totalBytes));

const width = String(maxNumber).length + 1;

function formatLine(counts, label) {
  const parts = counts.map((n) => String(n).padStart(width, " "));
  return parts.join("") + " " + label;
}

for (const { filePath, lines, words, bytes } of results) {
  const counts = getCounts(lines, words, bytes);
  process.stdout.write(formatLine(counts, filePath) + "\n");
}

if (results.length > 1) {
  const totals = getCounts(totalLines, totalWords, totalBytes);
  process.stdout.write(formatLine(totals, "total") + "\n");
}
