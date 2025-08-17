import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("my-ls")
  .description("Reimplementation of the Unix `ls` command with -1 and -a options")
  .option("-1", "list one file per line")
  .option("-a", "include hidden files")
  .argument("[directory]", "directory to list");

program.parse();

const options = program.opts();

const directory = program.args[0] || "."; // Use current directory as default if no argument is provided

const files = await fs.readdir(directory);

const visibleFiles = options.a ? files : files.filter(file => !file.startsWith("."));

if (options["1"]) {
  for (const file of visibleFiles) {
    console.log(file);
  }
} else {
  console.log(visibleFiles.join("       "));
}
  