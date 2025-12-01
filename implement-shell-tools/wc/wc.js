
import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .option("-l", "Print only the line count")
  .option("-w", "Print only the word count")
  .option("-c", "Print only the byte count")
  .argument("<paths...>", "One or more file paths");

program.parse();

const opts = program.opts();
const paths = program.args;

async function wcFile(path) {
  const content = await fs.readFile(path, "utf8");

  const lines = content.split("\n").length;
  const words = content.trim().split(/\s+/).filter(Boolean).length;
  const bytes = Buffer.byteLength(content, "utf8");

  return { lines, words, bytes };
}

function formatOutput(counts, filename, opts) {
  if (opts.l) return `${counts.lines} ${filename}`;
  if (opts.w) return `${counts.words} ${filename}`;
  if (opts.c) return `${counts.bytes} ${filename}`;

  return `${counts.lines} ${counts.words} ${counts.bytes} ${filename}`;
}

async function main() {
  let total = { lines: 0, words: 0, bytes: 0 };
  let multipleFiles = paths.length > 1;

  for (const path of paths) {
    const counts = await wcFile(path);

    total.lines += counts.lines;
    total.words += counts.words;
    total.bytes += counts.bytes;

    console.log(formatOutput(counts, path, opts));
  }

  if (multipleFiles) {
    console.log(formatOutput(total, "total", opts));
  }
}

main();
