import { promises as fs } from "node:fs";
import process from "node:process";
import path from "node:path";
import { program } from "commander";

program
  .name("ls")
  .description("Shows files in directory")
  .option("-1", "list one file per line")
  .option(
    "-a",
    "Used to list all files, including hidden files, in the current directory"
  )
  .argument("[path]", "The file path to process");

program.parse();

const programArgv = program.args;

if (programArgv.length > 0) {
  console.log(programArgv);
  console.log("k");
}

// i'm not using any arguments for now
// const argv = program.args;

const char = program.opts();

const pathToFile = process.argv[1];

// console.log(pathToFile);
const formattedPath = path.dirname(pathToFile);
// console.log(formattedPath);

async function listFiles() {
  if (char["1"]) {
    try {
      const files = await fs.readdir(formattedPath);
      const sortedOutput = files.sort((a, b) => a.localeCompare(b));
      files.forEach(function (file) {
        console.log(file);
      });
    } catch (err) {
      //is it goes to stderror
      console.error("Error reading directory:", err);
    }
  } else if (char["a"]) {
    try {
      const files = await fs.readdir(formattedPath);
      const formattedOutput = files.sort((a, b) => a.localeCompare(b));
      formattedOutput.unshift("..");
      formattedOutput.unshift(".");
      console.log(formattedOutput.join("             "));
    } catch (err) {
      //is it goes to stderror
      console.error("Error reading directory:", err);
    }
  }
}

listFiles();
