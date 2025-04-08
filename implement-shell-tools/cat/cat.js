import { promises as fs } from "fs";
import { program } from "commander";
// For handling "*.txt"
import * as glob from "glob";

// Set up program
program
    .name("cat command")
    .description("Implementing 'cat' command (-n, -b flags) functionality")
    .argument("<path...>", "Path")
    .option("-n", "Display line numbers")
    .option("-b", "Display line numbers only for non-empty lines")
    .parse(process.argv)

// Function to print file contents with the flags
async function displayFileContents(filePath, displayLineNumbers = false, displayNonEmptyLineNumbers = false) {
    try {
        // Read the file content
        let content = await fs.readFile(filePath, "utf-8");
        // Split content into array based on new lines
        let arrayContentLines = content.split("\n");
        // If last line is emty, remove it
        while (arrayContentLines.length > 0 && arrayContentLines[arrayContentLines.length - 1].trim() === "") {
            arrayContentLines.pop();
        }       

        // Map through all lines and apply different conditions depend on chosen flag.
        arrayContentLines = arrayContentLines.map(line => {
            if (displayNonEmptyLineNumbers) {
                if (line.trim()) {
                    console.log(`     ${lineNumber++}  ${line}`);
                } return "";
            } else if (displayLineNumbers) {
                console.log(`     ${lineNumber++}  ${line}`);
            } else{
                console.log(line);
            }            
        });        
    }
    catch (error) {
        console.error(`Error reading directory: ${error.message}`);
    }
}

//Get user inputs from command line
const filePaths = program.args;
const displayLineNumbers = program.opts().n;
const displayNonEmptyLineNumbers = program.opts().b;

// Declare and assign line number for printing line with numbers
let lineNumber = 1;

const arrayFilePaths = [];

// Loop through the array with paths to handle "*"
for (const filePath of filePaths) {
    // if filePath includes "*", use glob and push files to thr array
    if (filePath.includes("*")) {
        arrayFilePaths.push(...await glob(filePath));
    } else {
        arrayFilePaths.push(filePath);
    }
}

// Handling multiply file processing using Promise.all and map()
await Promise.all(arrayFilePaths.map(filePath => displayFileContents(filePath, displayLineNumbers, displayNonEmptyLineNumbers)));
