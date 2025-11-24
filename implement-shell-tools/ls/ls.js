import { program } from "commander";
import { promises as fs } from "node:fs";
import path from "node:path";

program
  .name("node-ls")
  .description("A Node.js implementation of the Unix ls command")
  .option("-1", "list one file per line")
  .option(
    "-a, --all",
    "include directory entries whose names begin with a dot (.)"
  )
  .argument("[directory]", "The file path to process");
program.parse();

const paths = program.args;

const directory = paths.length === 0 ? "." : paths[0];

let entries = await fs.readdir(directory);
console.log(entries.join("  "));


// entries.forEach((entry) => {
//   console.log(entry);
// });

// Read directory entries
// console.log(entries);
// for (const directory of directories) {

//   console.log(entries);
// }

// console.log(entries);

// --- Read directory contents ---
