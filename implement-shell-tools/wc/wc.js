import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
    .name("wc command")
    .description("Implementing 'wc' command")
    .option("-l", "show line count")
    .option("-w", "show word count")
    .option("-c", "show character count")
    .argument("<paths...>", "files to read");

program.parse();

const paths = program.args;
const options = program.opts();


function formatCounts(lines, words, chars, options) {
  let result = "";

  if (options.l || options.w || options.c) {
    if (options.l) result += `${lines}L  `;
    if (options.w) result += `${words}W  `;
    if (options.c) result += `${chars}Char  `;
  } else {
    result += `${lines}L ${words}W ${chars}Char `;
  }

  return result;
}

let totalLines = 0;
let totalWords = 0;
let totalChars = 0;

for (const path of paths) {
  const content = await fs.readFile(path, "utf-8");

  const lineCount = (content.match(/\n/g) || []).length;
  const wordCount = content.trim().split(/\s+/).length;
  const charCount = content.length;

  totalLines += lineCount;
  totalWords += wordCount;
  totalChars += charCount;

  const output = formatCounts(lineCount, wordCount, charCount, options);

  console.log(`${output}${path}`);
}

if (paths.length > 1) {
  const totalOutput = formatCounts(totalLines, totalWords, totalChars, options);

  console.log(`${totalOutput}total`);
}