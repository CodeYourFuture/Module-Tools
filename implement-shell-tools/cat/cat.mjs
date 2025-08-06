import { program } from "commander";
import {promises as fs} from "node:fs";

program
  .name("cat")
  .description("read, display, and concatenate text files.")
  .option("-n", " Number all output lines.")
  .option("-b", " Number non-blank output lines.")
  .arguments("<paths...>"); // allow more file paths

program.parse();

const options = program.opts();
const paths = program.args;

let hadError = false;
for(const path of paths){
    let content;
    try {
        content = await fs.readFile(path, "utf-8")
    } catch(err) {
        console.error(`Error reading file "${path}": ${err.message} `);
        hadError = true;
        continue;
    }

    // split file into lines
    let lines = content.replace(/\n$/, "").split("\n");
    let lineNum = 1;

    for (const line of lines){
        if(options.b){
            if(line.trim() !== ""){
                console.log(`${lineNum.toString().padStart(5)}  ${line}`)
                lineNum++;
            } else {
                console.log("");
            }
        } else if(options.n){
            console.log(`${lineNum.toString().padStart(5)}  ${line}`)
            lineNum++;
        } else{
            console.log(`${line}`)
        }
}
}

if (hadError) process.exit(1);