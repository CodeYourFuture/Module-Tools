import { program } from "commander";
import process from "node:process";
import { promises as fs } from "node:fs";

const args = process.argv.slice(2);

function removeEndEmptyLine(arr) {
  return arr[arr.length - 1] === "" ? arr.slice(0, -1) : arr;
}

async function createLineWordsCharCountForFile(path) {
  const content = await fs.readFile(path, { encoding: "utf-8" });
  const arrForLineCount = removeEndEmptyLine(content.split("\n"));
  const lineCount = arrForLineCount.length;
  const arrForWordsCount = arrForLineCount.flatMap((element) =>
    element.split(" ").filter((word) => word !== "")
  );

  const charArray = content.split("");
  const wordsCount = arrForWordsCount.length;
  const charCount = charArray.length;

  return `${lineCount} ${wordsCount} ${charCount} ${path}`;
}

async function createLineWordsCharCountForFiles() {
  const files = await Promise.all(args.map(createLineWordsCharCountForFile));
  files.forEach((file) => console.log(file));
}

createLineWordsCharCountForFiles();
