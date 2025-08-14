import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("my-wc")
  .description("Reimplementation of the Unix `wc` command supporting -l, -w, and -c flags")
  .option("-l", "show line count")
  .option("-w", "show word count")
  .option("-c", "show character count")
  .argument("<files...>", "files to read");

program.parse();

const options = program.opts();
const filePaths = program.args;

let totalLines = 0;
let totalWords = 0;
let totalChars = 0;

for (const filePath of filePaths) {
  const content = await fs.readFile(filePath, "utf-8");

  const lineCount = content.split("\n").length;
  const wordCount = content.trim().split(/\s+/).length;
  const charCount = content.length;

  totalLines += lineCount;
  totalWords += wordCount;
  totalChars += charCount;

  let output = "";

  if (options.l || options.w || options.c) {
    if (options.l) output += `${lineCount} `;
    if (options.w) output += `${wordCount} `;
    if (options.c) output += `${charCount} `;
  } else {
    output += `${lineCount} ${wordCount} ${charCount} `;
  }

  console.log(`${output}${filePath}`);
}

if (filePaths.length > 1) {
  let totalOutput = "";

  if (options.l || options.w || options.c) {
    if (options.l) totalOutput += `${totalLines} `;
    if (options.w) totalOutput += `${totalWords} `;
    if (options.c) totalOutput += `${totalChars} `;
  } else {
    totalOutput += `${totalLines} ${totalWords} ${totalChars} `;
  }

  console.log(`${totalOutput}total`);
}
