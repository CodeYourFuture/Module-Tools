import { program } from "commander";
import process from "node:process";
import { promises as fs } from "node:fs";

const args = process.argv.slice(2);

const path = args[0];
const content = await fs.readFile(path, { encoding: "utf-8" });
const arrForLineCount = content.split("\n");
const lineCount = arrForLineCount.length - 1;
const arrForWordsCount = arrForLineCount.flatMap((element) =>
  element.split(" ")
);
const charArray = arrForLineCount.flatMap((element) => element.split(""));
const wordsCount = arrForWordsCount.length - 1;
const charCount = charArray.length + 1;

console.log(`${lineCount} ${wordsCount} ${charCount} ${args[0]}`);
