import { program } from "commander";
import { promises as fs } from "node:fs";

//config the program
program
  .name("wc")
  .description(
    "The wc utility displays the number of lines, words, and bytes contained in each input file, or standard input"
  )
  .argument("<path>", "The file path to process");

//interpret the program
program.parse();

//use the parsed data
const path = program.args[0];

//read the file
const content = await fs.readFile(path, "utf-8");

//count lines
const lines = content.split("\n").length - 1;

//count words split by any whitespace
const words = content.split(/\s+/).filter((word) => word.length > 0).length;

//count character
const characters = content.length;

console.log(`${lines} ${words} ${characters} ${path}`);
