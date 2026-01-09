import process from "node:process";
import { promises as fs } from "node:fs";
import { program } from "commander";

program
  .name("list-files-in-directory")
  .description("List all files and directories in a directory")
  .argument("<path>", "The file path to process")
  .option("-1, --one", "Output one entry per line")
  .option("-a", "List all files & directories, including hidden ones");

program.parse();

const path = program.args[0];

const options = program.opts();

if (!path) {
    console.error("Error: No directory path was provided.");
    process.exit(1);
}

const directoryContent;

try {
    directoryContent = await fs.readdir(path);   
} catch (err) {
    console.error(`Error reading directory: ${err.message}`);
    process.exit(1);
}

let allContent = directoryContent;

if (!options.a) {
    allContent = directoryContent.filter(name => !name.startsWith("."));
}

for (const item of allContent) {
    if (options.one) {
        process.stdout.write(item + "\n");
    } else {
        process.stdout.write(item + "  ");
    }
    }



    
