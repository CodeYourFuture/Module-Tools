import { program } from "commander";
import { promises as fs } from "node:fs";

//config the program
program
  .name("ls")
  .description("list directory contents")
  .option("-1, --one", "Force output to be one entry per line")
  .option(
    "-a, --all",
    "shows all the files including the hidden ones which start with a dot"
  )
  .argument("[directory]", "Directory to list", "."); // "." means current directory

//interpret the program
program.parse();

// Get the directory argument (first argument in program.args array)
// If no argument provided, default to current directory "."
const directory = program.args[0] || ".";

//read the directory to get array of filenames
const files = await fs.readdir(directory);

//check for flags
const hasAflag = program.opts().all;

// Filter the files array BEFORE looping
// If hasAflag is true, keep all files
// If hasAflag is false, remove files that start with "."

const fileToShow = hasAflag 
? files
: files.filter(file => !file.startsWith("."))


//print each file on its own line
// Note: console.log(files) would print the entire array like: ['file1', 'file2']
// Loop prints each individually on separate lines

for (const file of fileToShow) {
    console.log(file)
}