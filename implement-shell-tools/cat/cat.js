import { program } from "commander";
import process from "node:process";
import { promises as fs } from "node:fs";

program
    .name("cat")
    .description("print the content of file")
    .option("-n , --line-numbers","Number the output lines, starting at 1")
    .argument("<path>", "The file path to process");
program.parse();

const argv = program.args;
if (argv.length != 1) {
    console.error(`Expected exactly 1 argument (a path) to be passed but got ${argv.length}.`);
    process.exit(1);
}

const options = program.opts();
const path = argv[0];
const content = await fs.readFile(path, "utf-8");
if (options.lineNumbers) {
    const lines= content.split(/\r?\n/);
    lines.forEach((line, index) => {
        console.log(index+1, line)
    });
   
} else {
    
    process.stdout.write(content);
}
