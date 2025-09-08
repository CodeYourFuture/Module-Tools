import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";
import path from "node:path";

program
  .name("ls")
  .description(
    `For each operand that names a file of type directory, ls displays the names of files contained within that directory, as well as any requested, associated information.
        \nIf no operands are given, the contents of the current directory are displayed. 
        \nIf more than one operand is given, non-directory operands are displayed first; directory and non-directory operands are sorted separately and in lexicographical order.`
  )
  .option("-1, --one-per-line", "output one entry per line.")
  .option("-a, --all", "shows hidden files")
  .argument("[paths...]", "The file paths to process");

program.parse();

const options = program.opts();
const arg = program.args;
let currentDirName = process.cwd();

async function listDirectory(currentDirName) {
  try {
    const files = await fs.readdir(currentDirName);
    let output = [];
    files.forEach((file) => {
      if (!options["all"] && file[0] === ".") {
        return;
      } else {
        output.push(file);
      }
    });
    output.sort();
    options.onePerLine
      ? output.forEach((file) => {
          console.log(file);
        })
      : console.log(output.join("  "));
  } catch (err) {
    if (err.code === "ENOENT") {
      console.error(`Error: The directory "${currentDirName}" does not exist.`);
    } else if (err.code === "ENOTDIR") {
      console.error(`Error: "${currentDirName}" is not a directory.`);
    } else {
      console.error(`Error listing ${currentDirName}: ${err.message}`);
    }
  }
}

if (arg[0]) {
  for (const dirName of arg) {
    try {
      const dirPath = path.join(currentDirName, dirName);
      console.log(dirName + ":");
      await listDirectory(dirPath);
    } catch (err) {
      console.log("Path should be a string.");
    }
  }
} else {
  try {
    await listDirectory(currentDirName);
  } catch (err) {
    console.log("Path should be a string.");
  }
}
