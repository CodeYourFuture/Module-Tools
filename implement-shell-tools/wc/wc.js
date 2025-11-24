import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";
import { stat } from "node:fs/promises";

program
  .name("count-containing-lines-words-characters")
  .description("Counts lines, words or characters in a file (or all files) inside a directory")
  .option("-l, --line", "The number of lines in each file")
  .option("-w, --word", "The number of words in each file")
  .option("-c, --character", "The number of characters in each file")
  .argument("<path...>", "The file path to process");

program.parse();

const argv = program.args;

const path = argv[0];

const options = program.opts();


if (argv.length < 1) {
    console.error("You must pass at least one path!");
    process.exit(1);
}

function counter(item) {
  const lines = item.trim().split("\n").length;
  const words = item.split(/\s+/).filter(Boolean).length;
  const characters = item.length;
  return { lines, words, characters };
}

let totalLines = 0;
let totalWords = 0;
let totalCharacters = 0;
let fileCount = 0;

for (const path of argv) {
    const pathInfo = await stat(path);

if (pathInfo.isFile()) {
    const content = await fs.readFile(path, "utf-8");
    const stats = counter(content);
    if (options.line) {
        console.log(`${stats.lines} ${path}`);
    } else if (options.word) {
        console.log(`${stats.words} ${path}`);
    } else {
        console.log(`${stats.characters} ${path}`);
    }

    totalLines += stats.lines;
    totalWords += stats.words;
    totalCharacters += stats.characters;
    fileCount++;

} else if (pathInfo.isDirectory()) {
    const files = await fs.readdir(path);
    for (const file of files) {
        const filePath = `${path}/${file}`;
        const fileContent = await fs.readFile(filePath, "utf-8");
        const stats = counter(fileContent);

        if (options.line) {
            console.log(`${stats.lines} ${filePath}`);
        } else if (options.word) {
           console.log(`${stats.words} ${filePath}`); 
        } else {
          console.log(`${stats.characters} ${filePath}`);  
        }

        totalLines += stats.lines;
        totalWords += stats.words;
        totalCharacters += stats.characters;
        fileCount++;
    }
}

}

if (fileCount > 1) {
    if (options.line) {
        console.log(`${totalLines} total`);
    } else if (options.word) {
      console.log(`${totalWords} total`);
    } else {
       console.log(`${totalCharacters} total`); 
    }
}