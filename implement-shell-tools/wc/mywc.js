import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("mywc")
  .description(
    "Counts lines, words, and bytes in files like the Unix wc command"
  )
  .option("-l", "counts the number of lines")
  .option("-w", "counts words")
  .option("-c", "counts bytes")
  .argument("<files...>", "Files to count");

program.parse();

const options = program.opts();
const files = program.args; 

// If there are no given flags, default to counting lines, words and bytes like the Unix wc command
if (!options.l && !options.w && !options.c) {
  options.l = true;
  options.w = true;
  options.c = true;
}

const showLines = options.l;
const showWords = options.w;
const showBytes = options.c;

// To support multiple files and a total
let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

for (const file of files) {
  try {
    const content = await fs.readFile(file, "utf-8");

    const lineCount = content.split("\n").length - 1;
    const wordCount = content.trim().split(/\s+/).filter(Boolean).length;
    const byteCount = Buffer.byteLength(content, "utf-8");

    totalLines += lineCount;
    totalWords += wordCount;
    totalBytes += byteCount;

    let output = "";
    if (showLines) output += `${lineCount.toString().padStart(8)}`;
    if (showWords) output += `${wordCount.toString().padStart(8)}`;
    if (showBytes) output += `${byteCount.toString().padStart(8)}`;
    output += ` ${file}`;

    console.log(output);
  } catch (err) {
    console.error(`Error reading file ${file}: ${err.message}`);
  }
}

// If multiple files were given, show the total
if (files.length > 1) {
  let totalOutput = "";
  if (showLines) totalOutput += `${totalLines.toString().padStart(8)}`;
  if (showWords) totalOutput += `${totalWords.toString().padStart(8)}`;
  if (showBytes) totalOutput += `${totalBytes.toString().padStart(8)}`;
  totalOutput += " total";

  console.log(totalOutput);
}