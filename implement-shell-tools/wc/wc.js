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

  const arrForWordsCount = arrForLineCount.flatMap((element) =>
    element.split(" ").filter((word) => word !== "")
  );

  const charArray = content.split("");

  const lineCount = arrForLineCount.length;
  const wordsCount = arrForWordsCount.length;
  const charCount = charArray.length;

  return `${lineCount} ${wordsCount} ${charCount} ${path}`;
}

async function createLineWordsCharCountForFiles() {
  const files = await Promise.all(args.map(createLineWordsCharCountForFile));
  files.forEach((file) => console.log(file));
  const aggregatedFilesData = aggregateFileData(files);
  console.log(
    `${aggregatedFilesData[0]} ${aggregatedFilesData[1]} ${aggregatedFilesData[2]} total`
  );
}

function aggregateFileData(files) {
  const digits = files.map((element) =>
    element.split(" ").slice(0, -1).map(Number)
  );
  const sums = digits[0].map((_, colIndex) =>
    digits.reduce((sum, row) => sum + row[colIndex], 0)
  );
  return sums;
}

createLineWordsCharCountForFiles();
