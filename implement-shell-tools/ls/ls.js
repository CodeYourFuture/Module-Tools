import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("list-files-in-directory")
  .description("Implement ls command to list files in directory")
  .option("-1, --one-per-line", "list files one per line")
  .option("-a, --allFiles", "list all files including hidden ones")
  .argument("[paths...]", "File paths to process");

program.parse(process.argv);

// options and path from commander.
const opts = program.opts();

let paths = program.args; // array of paths user typed
if (paths.length === 0) {
  paths = ["."];
}

for (const directoryPath of paths) {
  let entries;
  try {
    entries = await fs.readdir(directoryPath);
  } catch (err) {
    console.error(`ls: cannot access '${directoryPath}': ${err.message}`);
    continue; // move to next path if this one fails
  }

  if (!opts.allFiles) {
    entries = entries.filter((name) => !name.startsWith("."));
  }

  if (opts.onePerLine) {
    entries.forEach((name) => {
      console.log(name);
    });
  } else {
    //print files in one line if -1 is not used
    console.log(entries.join(" "));
  }
}
