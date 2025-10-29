import { program } from "commander";
import { promises as fs } from "node:fs";

program
    .name("ls command")
    .description("Implementing 'ls' command")
    .option("-1", "list one file per line")
    .option("-a", "include hidden files")
    .argument("[directory]", "Directory to list");

program.parse();

const directory = program.args[0] || ".";  //current directory as a defult if no directory provided
const allFiles = program.opts().a;
const listPerLine = program.opts()["1"];



const files = await fs.readdir(directory);
const visibleFiles = allFiles ? files : files.filter(file => !file.startsWith("."));

if (listPerLine){
    for (const file of visibleFiles){
        console.log(file)
    }
} else {
        console.log(visibleFiles.join("     "))
    }

