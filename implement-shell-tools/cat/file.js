import { program } from "commander";
import {promises as fs} from "node:fs"



 //configuring the program here to run flags.

program
  .name("cat")
  .description("Concatenate and print files")
  .option("-n, --number", "Number all output lines")
  .option("-b, --number-nonblank", "Number non-blank output lines") 
  .argument("<files...>", "File paths to display")
  .parse(process.argv);//Parse command line arguments (reads process.argv and interprets it)
  
const options = program.opts(); 
const files = program.args; // Array of file paths passed as arguments

let lineNumber = 1; // shared across all files, like GNU cat -n)

for (const file of files) {
  const content = await fs.readFile(file, "utf-8"); 
  const lines = content.split("\n");

  for (const line of lines) {
   
    if (options.number) {
      console.log(`${lineNumber.toString().padStart(6)}  ${line}`); // adding padding for formatting 
      lineNumber++;
    }  
    else if (options.numberNonblank) { // -b
      if (line.trim() === "") {
        console.log(line);
      } else {
        console.log(`${lineNumber.toString().padStart(6)}  ${line}`);
        lineNumber++;
      }
    } else {
      console.log(line);  
    } 
    }
  }



