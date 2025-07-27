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

let pathToFile = "";

const programArgv = program.args;

(async () => {
  if (programArgv.length === 1) {
    pathToFile = programArgv[0];
    try {
      const stats = await fs.stat(pathToFile);
      if (stats.isFile()) {
        console.log("is file ? " + stats.isFile());
        await listFiles("file");
      } else if (stats.isDirectory()) {
        console.log("is directory? " + stats.isDirectory());

        listFiles("directory");
      } else {
        console.error("Not a file or directory.");
      }
    } catch (err) {
      console.error("Invalid path:", err.message);
    }
  } else if (programArgv.length === 0) {
    pathToFile = process.cwd();
    await listFiles("directory");
  } else {
    console.error(
      `Expected no more than 1 argument (sample-files) but got ${programArgv.length}.`
    );
  }
})();

const flag_1 = (files) => {
  try {
    files.forEach(function (file) {
      console.log(file);
    });
  } catch (err) {
    //is it goes to stderror
    console.error("Error reading directory:", err);
  }
};

const flag_a = (files) => {
  try {
    files.unshift("..");
    files.unshift(".");
    return files;
  } catch (err) {
    //is it goes to stderror
    console.error("Error reading directory:", err);
  }
};

async function listFiles(type) {
  try {
    let formattedPath = "";
    if (type == "directory") {
      formattedPath = pathToFile;
    } else if (type == "file") {
      formattedPath = path.dirname(pathToFile);
    }
    const char = program.opts();
    const files = await fs.readdir(formattedPath);
    const sortedOutput = files.sort((a, b) => a.localeCompare(b));

    if (char["1"] && char["a"]) {
      flag_1(flag_a(sortedOutput));
    } else if (char["a"]) {
      console.log(flag_a(sortedOutput).join("     "));
    } else if (char["1"]) {
      flag_1(sortedOutput);
    }
  } catch (err) {
    console.error("Error reading directory:", err);
  }
}
