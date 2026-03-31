//On macOS (BSD cat), the -n option resets numbering for each file, so multiple files start again at 1,
//when you run cat -n sample-files/*.txt
//This Node.js script mimics GNU cat, where -n continues numbering across all files instead of restarting.
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
  

//Constants
const paddingWidth = 6; // width for line number padding

// Helper function to format a line with numbering
function formatLine(line, lineNumber, numberAll, numberNonBlank) {
  const numbered =`${lineNumber.toString().padStart(paddingWidth)}  ${line}`;
  if (numberAll) {
    return numbered
  }
  if (numberNonBlank) { 
    return line.trim() === "" ? line : numbered; 
  } 
  return line;
 }
const options = program.opts(); 
const files = program.args; // Array of file paths passed as arguments

let lineNumber = 1; // shared across all files

for (const file of files) {
  const content = await fs.readFile(file, "utf-8"); 
  let lines = content.split("\n");
  // Remove trailing empty line if file ends with newline
  if (lines.length > 0 && lines[lines.length - 1] === "") {
    lines.pop();
  }

  for (const line of lines) {
    const formatted = formatLine(line, lineNumber, options.number, options.numberNonblank);
    console.log(formatted);

    // Increment line number if numbering applies
    if (options.number || (options.numberNonblank && line.trim() !== "")) {
      lineNumber++;
    }
  }
}