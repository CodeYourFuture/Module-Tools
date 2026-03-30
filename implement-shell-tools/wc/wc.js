import { program } from "commander";
import * as fs from "node:fs";
import process from "node:process";
import path from "node:path";

program
  .name("wc")
  .description(`word, line, character, and byte count`)
  .option(
    "-l, --lines",
    "The number of lines in each input file is written to the standard output."
  )
  .option(
    "-w, --words",
    "The number of words in each input file is written to the standard output."
  )
  .option(
    "-c, --bytes",
    "The number of bytes in each input file is written to the standard output."
  )
  .argument("<paths...>", "The file paths to process");

program.parse();

const options = program.opts();
const arg = program.args;
let currentDirName = process.cwd();

let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

function countLines(content) {
  let counter = 0;
  for (const line of content.split("\n")) {
    counter += 1;
  }
  return counter - 1;
}

function countWords(content) {
  let counter = 0;
  for (const word of content.split(" ")) {
    for (const w of word.split("\n")) {
      if (w) {
        counter += 1;
      }
    }
  }
  return counter;
}

function countBytes(content) {
  let size = new Blob([content]).size;
  return size;
}

async function fileContentInfo(filePath, file) {
  try {
    let content = await fs.promises.readFile(filePath, "utf-8");
    let output = "";
    if (Object.keys(options).length == 0) {
      let numLines = countLines(content);
      let numWords = countWords(content);
      let numBytes = countBytes(content);
      output += numLines + " ";
      output += numWords + " ";
      output += numBytes + " ";
      totalLines += numLines;
      totalWords += numWords;
      totalBytes += numBytes;
    }
    if (options.lines) {
      let numLines = countLines(content);
      output += numLines + " ";
      totalLines += numLines;
    }
    if (options.words) {
      let numWords = countWords(content);
      output += numWords + " ";
      totalWords += numWords;
    }
    if (options.bytes) {
      let numBytes = countBytes(content);
      output += numBytes + " ";
      totalBytes += numBytes;
    }
    output += file;
    console.log(output);
  } catch (err) {
    console.log(err);
  }
}

async function main() {
  const promises = arg.map((argument) => {
    const filePath = path.join(currentDirName, argument);
    return new Promise((resolve, reject) => {
      fs.stat(filePath, (err, stats) => {
        if (err) {
          if (err.code === "ENOENT") {
            console.error(`wc: ${argument}: read: No such file or directory`);
          } else {
            console.error(`wc: ${argument}: read: Error: ${err.message}`);
          }
          resolve();
        } else if (stats.isFile()) {
          fileContentInfo(filePath, argument).then(resolve);
        } else if (stats.isDirectory()) {
          console.log(`wc: ${argument}: read: Is a directory`);
          resolve();
        } else {
          console.error(`wc: ${argument}: read: Unknown file type`);
          resolve();
        }
      });
    });
  });
  await Promise.all(promises);
  if (Object.keys(options).length == 0) {
    console.log(totalLines, totalWords, totalBytes, "total");
  } else {
    let totalOutput = "";
    options.lines ? (totalOutput += totalLines + " ") : null;
    options.words ? (totalOutput += totalWords + " ") : null;
    options.bytes ? (totalOutput += totalBytes + " ") : null;
    console.log(totalOutput + "total");
  }
}

main();
