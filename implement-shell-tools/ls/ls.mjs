import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";
program
  .option("-1", "show one file per line")
  .option("-a", "show hidden files")     
  .argument("[dir]", "folder to list", ".");
program.action(async (dir) => {
  try {
    let files = await fs.readdir(dir); //read files from the reader
    if (!program.opts().a) {
      files = files.filter(name => !name.startsWith(".")); //if -a is not used remove hidden files
    }
    // If -1 is used, show one file per line
    if (program.opts()["1"]) {
      for (const file of files) {
        process.stdout.write(file + "\n");
      }
    } else {
      process.stdout.write(files.join(" ") + "\n"); //show files in one line separated by space
    }
  } catch (error) {
    console.error("Error:", error.message);
  }
});
program.parse(); //start reading input
