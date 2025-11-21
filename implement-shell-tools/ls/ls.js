import { program } from "commander";
import { promises as fs } from "node:fs";

//configuring 
program
  .name("ls")
  .description("list directory contents")
  .option("-1, --one", "Outputs are printed one entry per line")
  .option("-a, --all","Show all files including hidden files that start with a .")
  .argument("[directory]", "Directory to list", "."); // "." means current directory

//interpret the program
program.parse();
const options = program.opts();
const directory = program.args[0] || "."; //get dir arg- 1st arg in program.args array || if no arg default to current dir


let files = await fs.readdir(directory); //read the dir to get array of filenames


if (!options.all) { //Handle -a (include hidden files)
  files = files.filter(name => !name.startsWith("."));
}

if (options.one) { // Print each file on its own line
  for (const file of files) {
    console.log(file);
  }
}
else {
  console.log(files.join(" "));// Default: join with spaces (like ls without -1)
}