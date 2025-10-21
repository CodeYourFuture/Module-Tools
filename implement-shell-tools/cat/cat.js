import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
    .name("cat command")
    .description("Implementing 'cat' command")
    .option("-n", "The line numbers")
    .option("-b", "The line numbers only for non-empty lines")
    .argument("<paths...>", "The file paths to process");

program.parse();

const paths = program.args;
let lineNumber = 1;
const displayLineNumber = program.opts().n;
const displayNonEmptyLineNumber = program.opts().b;

for(const path of paths){
const content = await fs.readFile(path, "utf-8");
const lines = content.split("\n");
  for(const line of lines){
    if(displayLineNumber){
      console.log(`${String(lineNumber).padStart(6, ' ')}  ${line}`);
      lineNumber++;
    } else if (displayNonEmptyLineNumber) {
      if (line.trim()) {
        console.log(`${String(lineNumber).padStart(6, ' ')}  ${line}`);
        lineNumber++;
      } else {
          console.log(line);

      }
     } 
  }
}