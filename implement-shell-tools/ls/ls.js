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
  .argument("[sample-files]", "The file path to process");

program.parse();

/* probably can be assigned by ternary operator */
let pathToFile = "";

const programArgv = program.args;
if (programArgv.length == 1) {
  pathToFile = programArgv[0];
} else if (programArgv.length == 0) {
  pathToFile = process.argv[1];
} else {
  console.error(
    `Expected no more than 1 argument (sample-files) to be passed but got ${argv.length}.`
  );
}

const char = program.opts();

const formattedPath = path.dirname(pathToFile);

async function listFiles() {
  /* can be rewritten using switch */
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
