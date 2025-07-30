import { Command } from "commander";
import process from "node:process";

program
    .name("ls")
    .description("Lists files in a directory like ls -1")
    .option("-1", "List one file per line") 
    .option("-a", "Show hidden files also") 
    .argument("[dir]", "The directory to list (optional, default: current)");

program.parse();


const argv = program.args;
const dir = argv[0] || "."; // default to current directory

// Arg validation: No more than 1 argument
if (argv.length > 1) {
    console.error(`Expected at most 1 argument (directory) but got ${argv.length}.`);
    process.exit(1);
}


