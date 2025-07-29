import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("wc")
  .description("Display numbers of line, words, and bytes in each file")
  .option("-l", "Number of lines")
  .option("-w", "Number of words")
  .option("-c", "Number of bytes")
  .argument("<path...>");

program.parse();

const options = program.opts();
const paths = program.args;

let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

for(const path of paths){
    let content;
    try{
        content = await fs.readFile(path, "utf-8");
    } catch (err){
        console.error(`Error reading file "${path}":`, err.message);
        continue;
    }

    const lines = content.replace(/\n$/, "").split("\n");
    
    const words = content.trim().split(/\s+/); // handles multiple spaces
    const { size } = await fs.stat(path);

    const lineCount = lines.length;
    const wordCount = words.length;
    const byteCount = size;

    totalLines += lineCount;
    totalWords += wordCount;
    totalBytes += byteCount;

    if(options.l) {
        console.log(`\t${lineCount} ${path}`);
    } else if(options.w) {
        console.log(`\t${wordCount} ${path}`);
    } else if(options.c) {
        console.log(`\t${byteCount} ${path}`)
    } else {
        console.log(`\t${lineCount}\t${wordCount}\t${size} ${path}`);
    }

}

if (paths.length > 1) {
  if (options.l) {
    console.log(`\t${totalLines} total`);
  } else if (options.w) {
    console.log(`\t${totalWords} total`);
  } else if (options.c) {
    console.log(`\t${totalBytes} total`);
  } else {
    console.log(`\t${totalLines}\t${totalWords}\t${totalBytes} total`);
  }
}