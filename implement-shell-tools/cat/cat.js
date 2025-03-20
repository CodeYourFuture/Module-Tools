import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
    .name("concatenate-and-print-files")
    .description("Concatenate and print files")
    .option('-b', 'number the non-blank output lines, starting at 1.')
    .option('-n', 'number all output lines, starting at 1.')
    .option('-s', 'remove multiple blank lines in the text.')
    .argument("<paths...>", "The file paths to process");

program.parse();
const options = program.opts()
const argvs = program.args;

if (options.n && options.b ){
    console.error(`Expected -n or -b option to be passed but got both.`);
    process.exit(1);
}

for (const path of argvs) {
    try {
        let content = await fs.readFile(path, "utf-8");
        const lines = content.split('\n')
        lines.pop()
        let number = 1
        if(content && content.trim()){
            if (options.s){
                content = content.replace(/\n{2,}/g, '\n');
            }
            for (const line of lines){
                if (options.n) {
                    console.log(number + ' ' + line)
                    number += 1
                }else if (line.trim() && options.b){
                    console.log(number + ' ' + line)
                    number += 1
                }
                else{
                    console.log(line)
                }
            }
        }
    }catch (err) {
        console.error(`Error reading ${path}: ${err.message}`);
        process.exit(1); 
    }
}
