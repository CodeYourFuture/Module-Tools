import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("wc")
  .description("Custom wc CLI - count lines, words, bytes")
  .argument("<file>", "File to process")
  .option("-l", "Print the number of lines")
  .option("-w", "Print the number of words")
  .option("-c", "Print the number of bytes")
  .parse();

const options = program.opts();
const filePath = program.args[0];

try {
  const data = await fs.readFile(filePath,"utf-8");
  


  const lineCount = data.split("\n").length;
  const wordCount = data.trim().split(/\s+/).length;
  const byteCount = data.length;

  const showAll = !options.l && !options.w && !options.c;

  
  const output = [];
  if (options.l || showAll) output.push(lineCount.toString().padStart(8));
  if (options.w || showAll) output.push(wordCount.toString().padStart(8));
  if (options.c || showAll) output.push(byteCount.toString().padStart(8));
  output.push(filePath);

  console.log(output.join(" "));
} catch (err) {
  console.error(`Error reading file "${filePath}":`, err.message);
  process.exit(1);
}