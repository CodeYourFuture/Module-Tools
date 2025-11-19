import { program } from "commander";
import { promises as fs } from "node:fs";

//config the program
program
  .name("ls")
  .description("list directory contents")
  .option("-1, --one", "Force output to be one entry per line")
  .argument("[directory]", "Directory to list", "."); // "." means current directory

//interpret the program
program.parse();

// Get the directory argument (first argument in program.args array)
// If no argument provided, default to current directory "."
const directory = program.args[0] || ".";

//read the directory to get array of filenames
const files = await fs.readdir(directory);



//print each file on its own line
// Note: console.log(files) would print the entire array like: ['file1', 'file2']
// Loop prints each individually on separate lines
for (const file of files) {
    console.log(file)
}
