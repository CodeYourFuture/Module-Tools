import { program } from "commander";
import { promises as fs } from "node:fs";

//configuring 
program
  .name("ls")
  .description("list directory contents")
  .option("-1, --one", "Outputs are printed one entry per line")
  .argument("[directory]", "Directory to list", "."); // "." means current directory

//interpret the program
program.parse();
const directory = program.args[0] || "."; //get dir arg- 1st arg in program.args array || if no arg default to current dir


const files = await fs.readdir(directory); //read the dir to get array of filenames



//print each file on its own line
for (const file of files) { // Loop prints each individually on separate lines
    console.log(file)
}