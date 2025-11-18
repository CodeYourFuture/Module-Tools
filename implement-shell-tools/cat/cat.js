import {program} from "commander";
import {promises as fs} from "node:fs"


//here we Configure the program: what flags and arguments it accepts
// .option("short, long", "description")
//The < > brackets mean "required"

program
  .name("cat")
  .description("concatenate and print files")
  .option("-n, --number", "Number all output lines")
  .argument("<path>", "The file path to process");

// here Parse command line arguments (reads process.argv and interprets it)
program.parse();


// Get the parsed values
const path = program.args[0]; // The filename user provided
const hasNumberFlag = program.opts().number;    // True if user used -n flag

//read the file
const content = await fs.readFile(path, "utf-8")

// Output with or without line numbers
if (hasNumberFlag) {
  // Add line numbers to each line
  const lines = content.split("\n"); // Split into array of lines
  const numberedLines = lines.map((line, index) => {
    const numberOfLine = index + 1; // Convert 0-based index to 1-based line number
    return `${numberOfLine} ${line}`; // Format: "     1  Hello"
  });
  console.log(numberedLines.join("\n")); // Join back with newlines
} else {
  // Just print the file as-is
  console.log(content);
}






