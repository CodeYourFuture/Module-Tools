import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("wc")
  .description("Count lines, words, and bytes in files")
  .option("-l, --lines", "Only print line counts")
  .option("-w, --words", "Only print word counts")
  .option("-c, --bytes", "Only print byte counts")
  .argument("<files...>", "One or more files to process");
await program.parseAsync();

const files = program.args;
const options = program.opts();

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
        
        if (options.lines) {
            console.log(`${lines} ${file}`);
        } else if (options.words) {
            console.log(`${words} ${file}`);
        }else if (options.bytes) {
            console.log(`${bytes} ${file}`);
        }else {
            console.log(`${lines} ${words} ${bytes} ${file}`);
        }

        totalLines += lines;
        totalWords += words;
        totalBytes += bytes;

    }catch (err) {
    console.error(`wc: ${file}: ${err.message}`);
  }
}

if (files.length > 1) {
    if (options.lines) {
        console.log(`${totalLines} total`)//if more then 1 file is
    }else if (options.words) {
        console.log(`${totalWords} total`);
    } else if (options.bytes) {
        console.log(`${totalBytes} total`);
    } else {
        console.log(`${totalLines} ${totalWords} ${totalBytes} total`);
    }
}
