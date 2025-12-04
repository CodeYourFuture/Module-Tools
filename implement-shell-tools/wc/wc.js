import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("wc command")
  .description("Implement wc command to count words and lines")
  .option("-l,", "show number of lines only")
  .option("-w,", "show number of words only")
  .option("-c,", "show number of characters only")
  .argument("[path...]", "The file path to process");

program.parse(process.argv);

const opts = program.opts();
let paths = program.args;

if (paths.length === 0) {
  console.error("wc: no file specified");
  process.exit(1);
}

let totals = { lines: 0, words: 0, chars: 0 };

for (const filePath of paths) {
  let content;
  try {
    content = await fs.readFile(filePath, "utf8");
  } catch (err) {
    console.error(`wc: cannot read file "${filePath}": ${err.message}`);
    continue; // move on to next path
  }

  const lineCount = content.split("n").length;

  const wordCount = content.split(/\s+/).filter(Boolean).length;

  const charCount = content.length;

  totals.lines += lineCount;
  totals.words += wordCount;
  totals.chars += charCount;

  // Decide what to print depending on flags
  if (!opts.l && !opts.w && !opts.c) {
    console.log(`${lineCount} ${wordCount} ${charCount} ${filePath}`);
    continue;
  }

  if (opts.l) {
    console.log(`${lineCount} ${filePath}`);
  }

  if (opts.w) {
    console.log(`${wordCount} ${filePath}`);
  }

  if (opts.c) {
    console.log(`${charCount} ${filePath}`);
  }
}

//Print totals if there are multiple files
if (paths.length > 1) {
  if (!opts.l && !opts.w && !opts.c) {
    console.log(`${totals.lines} ${totals.words} ${totals.chars} total`);
  }

  if (opts.l) {
    console.log(`${totals.lines} total`);
  }

  if (opts.w) {
    console.log(`${totals.words} total`);
  }

  if (opts.c) {
    console.log(`${totals.chars} total`);
  }
}
