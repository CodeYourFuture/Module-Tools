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
  const hasBFlag = program.opts().numberNonBlank;

  //read the file for each argument
  const content = await fs.readFile(path, "utf-8");
  // Output with or without line numbers
  if (hasNumberFlag) {
    // Add line numbers to each line
    const lines = content.split("\n"); // Split into array of lines
    const numberedLines = lines.map((line) => {
      lineNumber = lineNumber + 1;
      return `${lineNumber} ${line}`; // Format: "     1  Hello"
    });
    console.log(numberedLines.join("\n")); // Join back with newlines
  } else if (hasBFlag) {
    const lines = content.split("\n");

    const numberedLines = lines.map((line) => {
      if (line.trim() === "") {
        return line;
      } else {
        lineNumber = lineNumber + 1;
        return ` ${lineNumber} ${line}`;
      }
    });
    console.log(numberedLines.join("\n"));
  } else {
    // Just print the file as-is
    console.log(content);
  }
}
