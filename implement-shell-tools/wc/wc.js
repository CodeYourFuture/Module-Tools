import { program } from "commander";
import { promises as fs } from "node:fs";

//config the program
program
  .name("wc")
  .description(
    "The wc utility displays the number of lines, words, and bytes contained in each input file, or standard input"
  )
  .option("-l, --lines", "count lines only")
  .option("-w, --words", "count words only")
  .option("-c, --bytes", "count bytes only")
  .argument("<path...>", "The file paths to process");

//interpret the program
program.parse();

//initialise totals
let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

//check for flags
const hasLineFlag = program.opts().lines;
const hasWordFlag = program.opts().words;
const hasBytesFlag = program.opts().bytes;

// create output format function to avoid repetition
function formatOutput(lines, words, bytes, path) {
  if (hasLineFlag) {
    console.log(`${lines} ${path}`);
  } else if (hasWordFlag) {
    console.log(`${words} ${path}`);
  } else if (hasBytesFlag) {
    console.log(`${bytes} ${path}`);
  } else {
    console.log(`${lines} ${words} ${bytes} ${path}`);
  }
}

//process each file

for (const path of program.args) {
  //read the file
  const content = await fs.readFile(path, "utf-8");

  //count lines
  const lines = content.split("\n").length - 1;

  //count words (split by any whitespace)
  const words = content.split(/\s+/).filter((word) => word.length > 0).length;

  //count bytes correctly especially important for non-ASCII characters
  const bytes = Buffer.byteLength(content, "utf-8");

  //Add to totals
  totalLines += lines;
  totalWords += words;
  totalBytes += bytes;

  formatOutput(lines, words, bytes, path);
}

if (program.args.length > 1) {
  formatOutput(totalLines, totalWords, totalBytes, "total");
}
