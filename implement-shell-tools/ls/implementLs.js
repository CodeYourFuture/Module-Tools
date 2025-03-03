import process from "node:process";
import { promises as fs } from "node:fs";
import { program } from "commander";

program
  .name("Implement ls")
  .description("Implements a version of the ls command")
  .option("-1, --one", "Output all files and directories each in a line")
  .option("-a, --hidden", "Output hidden files/directories")
  .argument("[paths...]", "the paths to be processed")
  .parse(process.argv);

const filePaths = program.args.length ? program.args : ["."];
const one = program.opts().one;
const hidden = program.opts().hidden;

filePaths.forEach(async (filePath) => {
  try {
    const files = await fs.readdir(filePath, { withFileTypes: true }); // is returned as a Dirent
    const filteredFiles = files
      .filter((file) => hidden || !file.name.startsWith("."))
      .map((file) => file.name);

    if (hidden) {
      filteredFiles.unshift(".", "..");
    }

    if (one) {
      filteredFiles.forEach((file) => console.log(file));
    } else {
      console.log(filteredFiles.join(" "));
    }
  } catch (err) {
    console.error(`Error reading directory ${filePath}:`, err.message);
  }
});
