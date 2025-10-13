import { program } from "commander";
import { readFileSync, existsSync } from "fs";
import process from "process";

program
  .name("wc")
  .description("Count lines, words, and characters in files")
  .argument("[files...]", "Files to process")
  .option("-l, --lines", "Count lines")
  .option("-w, --words", "Count words")
  .option("-c, --chars", "Count characters (bytes)");

program.parse(process.argv);

const options = program.opts();
const files = program.args.length ? program.args : ["/dev/stdin"];

function countFile(filePath, options) {
  let content = "";
  try {
    if (filePath === "/dev/stdin") {
      content = readFileSync(process.stdin.fd, "utf8");
    } else {
      if (!existsSync(filePath)) {
        console.error(`wc: ${filePath}: No such file or directory`);
        return null;
      }
      content = readFileSync(filePath, "utf8");
    }
  } catch (error) {
    console.error(`wc: ${filePath}: ${error.message}`);
    return null;
  }

  const lineCount = (content.match(/\n/g) || []).length;
  const wordCount = content.trim().split(/\s+/).filter(Boolean).length;
  const charCount = Buffer.byteLength(content, "utf8");

  return {
    file: filePath,
    lines: options.lines || (!options.words && !options.chars) ? lineCount : null,
    words: options.words || (!options.lines && !options.chars) ? wordCount : null,
    chars: options.chars || (!options.lines && !options.words) ? charCount : null,
  };
}

const results = [];
let totalLines = 0, totalWords = 0, totalChars = 0;
const hasMultipleFiles = files.length > 1;

for (const file of files) {
  const result = countFile(file, options);
  if (result) {
    results.push(result);
    if (result.lines !== null) totalLines += result.lines;
    if (result.words !== null) totalWords += result.words;
    if (result.chars !== null) totalChars += result.chars;
  }
}

results.forEach(result => {
  const output = [];
  if (result.lines !== null) output.push(result.lines.toString().padStart(8));
  if (result.words !== null) output.push(result.words.toString().padStart(8));
  if (result.chars !== null) output.push(result.chars.toString().padStart(8));
  console.log(output.join(" "), result.file);
});

if (hasMultipleFiles && results.length > 0) {
  const totalOutput = [];
  if (options.lines || (!options.words && !options.chars)) totalOutput.push(totalLines.toString().padStart(8));
  if (options.words || (!options.lines && !options.chars)) totalOutput.push(totalWords.toString().padStart(8));
  if (options.chars || (!options.lines && !options.words)) totalOutput.push(totalChars.toString().padStart(8));
  console.log(totalOutput.join(" "), "total");
}
