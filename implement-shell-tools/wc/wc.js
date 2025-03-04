import { program } from "commander";
import process from "node:process";
import { promises as fs } from "node:fs";

program
  .name("Implement wc")
  .description("Implements a version of the wc command")
  .option("-l, --line", "Counts file lines")
  .option("-c, --char", "Counts characters in file")
  .option("-w, --word", "Counts words in file")
  .argument("[paths...]", "The path/s to process")
  .parse(process.argv);

const args = program.args;

function removeEndEmptyLine(arr) {
  return arr[arr.length - 1] === "" ? arr.slice(0, -1) : arr;
}

const lineOption = program.opts().line;
const charOption = program.opts().char;
const wordOption = program.opts().word;

async function countLinesWordsCharsInFile(path) {
  const content = await fs.readFile(path, { encoding: "utf-8" });

  const lines = removeEndEmptyLine(content.split("\n"));

  const words = lines.flatMap((element) =>
    element.split(" ").filter((word) => word !== "")
  );

  const chars = content.split("");

  const numberOfLines = lines.length;
  const numberOfWords = words.length;
  const numberOFChars = chars.length;

  if (lineOption) {
    return `${numberOfLines} ${path}`;
  }

  if (charOption) {
    return `${numberOFChars} ${path}`;
  }

  if (wordOption) {
    return `${numberOfWords} ${path}`;
  }

  return `${numberOfLines} ${numberOfWords} ${numberOFChars} ${path}`;
}

async function createLineWordsCharCountForFiles() {
  const files = await Promise.all(args.map(countLinesWordsCharsInFile));
  files.forEach((file) => console.log(file));
  const aggregatedFilesData = aggregateFileData(files);

  if (aggregatedFilesData !== 0 && lineOption) {
    console.log(`${aggregatedFilesData[0]} total`);
    return;
  }

  if (aggregatedFilesData !== 0 && wordOption) {
    console.log(`${aggregatedFilesData[0]} total`);
    return;
  }

  if (aggregatedFilesData !== 0 && charOption) {
    console.log(`${aggregatedFilesData[0]} total`);
    return;
  }

  aggregatedFilesData !== 0
    ? console.log(
        `${aggregatedFilesData[0]} ${aggregatedFilesData[1]} ${aggregatedFilesData[2]} total`
      )
    : null;
}

function aggregateFileData(files) {
  const digits = files.map((element) =>
    element.split(" ").slice(0, -1).map(Number)
  );
  const sums =
    digits.length > 1
      ? digits[0].map((_, colIndex) =>
          digits.reduce((sum, row) => sum + row[colIndex], 0)
        )
      : 0;
  return sums;
}

createLineWordsCharCountForFiles();
