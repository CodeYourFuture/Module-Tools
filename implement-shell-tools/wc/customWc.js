import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("Custom-wc")
  .description("Custom-wc-that-works-like-wc")
  .option("-l, --lines", "Counting lines in the file")
  .option("-w, --words", "Counting words in the file")
  .option("-c, --characters", "Counting characters in the file")
  .argument("<path...>", "Path of file to process");

program.parse();

const argumentArray = program.args;
if (argumentArray.length === 0) {
  console.log(`We need at least one file path to process`);
  process.exit(1);
}

const pathArray = argumentArray;
const options = program.opts();

function padStartNumbers(...args) {
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

  if (pathArray.length > 1) {
    if (options.lines) {
      console.log(`${padStartNumbers(numberOfLines)} ${path}`);
    }
    if (options.words) {
      console.log(`${padStartNumbers(numberOfWords)} ${path}`);
    }
    if (options.characters) {
      console.log(`${padStartNumbers(numberOfCharacters)} ${path}`);
    }
  } else if (options.lines) {
    console.log(`${numberOfLines} ${path}`);
  } else if (options.words) {
    console.log(`${numberOfWords} ${path}`);
  } else if (options.characters) {
    console.log(`${numberOfCharacters} ${path}`);
  } else {
    console.log(
      `${padStartNumbers(numberOfLines, numberOfWords, numberOfCharacters)} ${path}`,
    );
  }
  totalOfLines += numberOfLines;
  totalOfWords += numberOfWords;
  totalOfCharacters += numberOfCharacters;
}

if (pathArray.length > 1) {
  if (options.lines) {
    console.log(`${padStartNumbers(totalOfLines)} total`);
  } else if (options.words) {
    console.log(`${padStartNumbers(totalOfWords)} total`);
  } else if (options.characters) {
    console.log(`${padStartNumbers(totalOfCharacters)} total`);
  } else {
    console.log(
      `${padStartNumbers(totalOfLines, totalOfWords, totalOfCharacters)} total`,
    );
  }
}
