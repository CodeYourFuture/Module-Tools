import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("wc")
  .description("Count lines, words, and bytes in files")
  .argument("<files...>", "One or more files to process");
await program.parseAsync();

const files = program.args;

function countContent(content){
    const lines = (content.match(/\n/g) || []).length;
    const words = content.trim().split(/\s+/).filter(Boolean).length;
    const bytes = Buffer.byteLength(content, 'utf-8');
    return {lines, words, bytes};
}

let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

for(const file of files){
    try{
        const content = await fs.readFile(file, "utf-8");
        const {lines, words, bytes } = countContent(content);
        console.log(`${lines} ${words} ${bytes} ${file}`);

        totalLines += lines;
        totalWords += words;
        totalBytes += bytes;

    }catch (err) {
    console.error(`wc: ${file}: ${err.message}`);
  }
}

if (files.length > 1) {
  console.log(`${totalLines} ${totalWords} ${totalBytes} total`);
}