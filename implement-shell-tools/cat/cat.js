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
  .argument("<path...>", "The file paths to process");

// here Parse command line arguments (reads process.argv and interprets it)
program.parse();

// Shared counter across all files for -n and -b flags
let lineNumber = 0;


// Process each file
for (const path of program.args) {
  const hasNumberFlag = program.opts().number; // True if user used -n flag
  const shouldNumberNonBlank = program.opts().numberNonBlank;

  //read the file for each argument
  const content = await fs.readFile(path, "utf-8");
  const lines = content.split("\n"); // Split into array of lines

  // Output with or without line numbers
  if (hasNumberFlag) {
    // Add line numbers to each line
    const numberedLines = lines.map((line) => {
      lineNumber = lineNumber + 1;
      return `${lineNumber} ${line}`; // Format: "     1  Hello"
    });
    console.log(numberedLines.join("\n")); // Join back with newlines
  } else if (shouldNumberNonBlank) {

    const numberedLines = lines.map((line) => {
      return line.trim() === "" ? line : `${++lineNumber} ${line}`;
    });
    console.log(numberedLines.join("\n"));
  } else {
    // Just print the file as-is
    console.log(content);
  }
}

