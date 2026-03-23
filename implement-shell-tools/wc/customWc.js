import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("Custom-wc")
  .description("Custom-wc-that-works-like-wc")
  .argument("<path...>", "Path of file to process");

program.parse();

const argumentArray = program.args;
if (argumentArray.length === 0) {
  console.log(`We need at least one file path to process`);
  process.exit(1);
}

const pathArray = argumentArray;
const path = pathArray[0];

function padStartNumbers(...args) {
  if (args.length != 3) {
    throw new Error(
      "It takes 3 arguments in order as numberOfLines, numberOfWords, numberOfCharacters",
    );
  }
  const space = [3, 4, 4];
  const numberStringArray = [];
  for (let index = 0; index < args.length; index++) {
    numberStringArray.push(String(args[index]).padStart(space[index], " "));
  }
  return numberStringArray.join("");
}

let totalOfLines = 0;
let totalOfWords = 0;
let totalOfCharacters = 0;

for (let path of pathArray) {
  let numberOfLines = 0;
  let numberOfWords = 0;
  let numberOfCharacters = 0;

  const file = await fs.readFile(path, "utf-8");
  numberOfCharacters = file.length;
  numberOfLines = file.split("\n").length - 1;
  const words = file.match(/\S+/g);
  numberOfWords = words ? words.length : 0;
  console.log(
    `${padStartNumbers(numberOfLines, numberOfWords, numberOfCharacters)} ${path}`,
  );
  totalOfLines += numberOfLines;
  totalOfWords += numberOfWords;
  totalOfCharacters += numberOfCharacters;
}

if (pathArray.length > 1) {
  console.log(
    `${padStartNumbers(totalOfLines, totalOfWords, totalOfCharacters)} total`,
  );
}
