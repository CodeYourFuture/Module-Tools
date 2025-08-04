import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("myls")
  .description("list file(s) in the directory, like the ls command")
  .option("-1", "list one file per line")
  .option("-a", "include hidden files")
  .argument("[directory]", "Directory to list", ".");

program.parse();

const options = program.opts();
const directory = program.args[0] || ".";

try {
  let files = await fs.readdir(directory);

  // if "-a" is used, include hidden files; those that start with "." 
  if (options.a) {
    files = [".", "..", ...files];
  }

  for (const file of files) {
    // if "-a" is not used, skip hidden files; those that start with "."
    if (!options.a && file.startsWith(".")) {
      continue;
    }

    console.log(file); // print file name; one file per line
  }
} catch (error) {
  console.error(`Error reading directory ${directory}:`, error.message);
  process.exit(1);
}