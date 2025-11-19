import { program } from "commander";
import { promises as fs } from "node:fs";

//config the program
program
  .name("wc")
  .description(
    "The wc utility displays the number of lines, words, and bytes contained in each input file, or standard input"
  )
  .argument("<path...>", "The file paths to process");

//interpret the program
program.parse();

//initialise totals
let totalLines = 0;
let totalWords = 0;
let totalCharacters = 0;

//process each file

for (const path of program.args) {
  //read the file
  const content = await fs.readFile(path, "utf-8");

  //count lines
  const lines = content.split("\n").length - 1;

  //count words (split by any whitespace)
  const words = content.split(/\s+/).filter((word) => word.length > 0).length;

  //count character
  const characters = content.length;

  //Add to totals
  totalLines += lines;
  totalWords += words;
  totalCharacters += characters;

  console.log(`${lines} ${words} ${characters} ${path}`);
}

if (program.args.length > 1) {
  console.log(`${totalLines} ${totalWords} ${totalCharacters} total`);
}
