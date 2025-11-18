import { program } from "commander";
import { promises as fs } from "node:fs";

//here we Configure the program: what flags and arguments it accepts
// .option("short, long", "description")
//The < > brackets mean "required"

program
  .name("cat")
  .description("concatenate and print files")
  .option("-n, --number", "Number all output lines")
  .option("-b, --numberNonBlank", "Number non-blank output lines")
  .argument("<path>", "The file path to process");

// here Parse command line arguments (reads process.argv and interprets it)
program.parse();

// Get the parsed values
const path = program.args[0]; // The filename user provided
const hasNumberFlag = program.opts().number; // True if user used -n flag
const hasBFlag = program.opts().numberNonBlank;

//read the file
const content = await fs.readFile(path, "utf-8");

// Output with or without line numbers
if (hasNumberFlag) {
  
  // Add line numbers to each line
  const lines = content.split("\n"); // Split into array of lines
  const numberedLines = lines.map((line, index) => {
    const lineNumber = index + 1; // Convert 0-based index to 1-based line number
    return `${lineNumber} ${line}`; // Format: "     1  Hello"
  });
  console.log(numberedLines.join("\n")); // Join back with newlines
} else if (hasBFlag) {
  console.log("Using -b flag!");
  let lineNumber = 0;
  const lines = content.split("\n");
  console.log("Total lines:", lines.length);
  const numberedLines = lines.map((line) => {
     console.log(`Line: "${line}", isEmpty: ${line.trim() === ""}`);  
    if (line.trim() === "") {
      return line;
    } else {
      lineNumber = lineNumber + 1;
      return ` ${lineNumber} ${line}`
    }
  });
console.log(numberedLines.join("\n"));
} else {
  // Just print the file as-is
  console.log(content);
}
