import { program } from "commander";
import { readFile } from "node:fs/promises";

program
  .name("wc")
  .description("Word, line, and byte count")
  .option("-l", "Print the newline counts")
  .option("-w", "Print the word counts")
  .option("-c", "Print the byte counts")
  .argument("<files...>", "Files to read")
  .parse();

const options = program.opts();
const files = program.args;

function countStats(text) {
  const lines = text.split("\n").length - 1;
  const words = text.trim().split(/\s+/).filter(Boolean).length;
  const bytes = Buffer.byteLength(text, "utf8");
  return { lines, words, bytes };
}

function formatOutput(stats, filename) {
  let output = "";
  const showAll = !options.l && !options.w && !options.c;

  if (options.l || showAll) output += stats.lines.toString().padStart(7);
  if (options.w || showAll) output += stats.words.toString().padStart(7);
  if (options.c || showAll) output += stats.bytes.toString().padStart(7);

  return output + " " + filename;
}

let total = { lines: 0, words: 0, bytes: 0 };

for (const file of files) {
  try {
    const text = await readFile(file, "utf8");
    const stats = countStats(text);

    total.lines += stats.lines;
    total.words += stats.words;
    total.bytes += stats.bytes;

    console.log(formatOutput(stats, file));
  } catch (err) {
    console.error(`wc: ${file}: ${err.message}`);
  }
}

if (files.length > 1) {
  console.log(formatOutput(total, "total"));
}
