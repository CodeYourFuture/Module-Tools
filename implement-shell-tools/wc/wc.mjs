import {program} from "commander";
import{promises as fs} from "node:fs";

program
.name("wc")
.description("counts lines, words, and bytes")
.option("-l, --line", "counts number of lines in the file")
.option("-w, --words", "counts number of words in the file")
.option("-c, --bytes", "counts number  of bytes in the file")
.argument("<filepath>")

program.parse();

const args= program.args;
const opts = program.opts();

if(args.length === 0){
    console.error("Error: Missing <filepath> argument.");
  program.help();
}

const path = args[0];
const content = await fs.readFile(path, "utf-8");


// function to count the number of lines in a files
function countLines(content){
const lines = content.split(/\r?\n/);
return lines.length;
}

//function to count the words
function countWords(content){
  const words = content.trim().split(/\s+/);
  return words.length;
}

//function to count the bytes
function countBytes(content){
  return Buffer.byteLength(content, "utf-8");
}

const lines = countLines(content);
const words = countWords(content);
const bytes = countBytes(content);

if (opts.line) {
  console.log(lines);
} else if (opts.words) {
  console.log(words, path);
} else if (opts.bytes) {
  console.log(bytes, path);
} else {
  console.log(lines, words, bytes, path);
}