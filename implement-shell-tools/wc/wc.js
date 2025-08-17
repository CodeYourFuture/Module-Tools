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

function formatCounts(lines, words, chars, options) {
  let result = "";

  if (options.l || options.w || options.c) {
    if (options.l) result += `${lines}  `;
    if (options.w) result += `${words}  `;
    if (options.c) result += `${chars}  `;
  } else {
    result += `${lines} ${words} ${chars} `;
  }
  
  return result;
}

let totalLines = 0;
let totalWords = 0;
let totalChars = 0;

for (const filePath of filePaths) {
  const content = await fs.readFile(filePath, "utf-8");

  const lineCount = (content.match(/\n/g) || []).length;
  const wordCount = content.trim().split(/\s+/).length;
  const charCount = content.length;

  totalLines += lineCount;
  totalWords += wordCount;
  totalChars += charCount;

  const output = formatCounts(lineCount, wordCount, charCount, options);

  console.log(`${output}${filePath}`);
}

if (filePaths.length > 1) {
  const totalOutput = formatCounts(totalLines, totalWords, totalChars, options);

  console.log(`${totalOutput}total`);
}
