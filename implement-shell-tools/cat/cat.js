import * as fs from "fs";
import { program } from "commander";
// For reading file line by line
import * as readline from "readline";
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
        // Create a readline interface to read file line by line
        const fileStream = fs.createReadStream(filePath, { encoding: 'utf-8' });
        const rl = readline.createInterface({
            input: fileStream,
            crlfDelay: Infinity
        });    
        
        // Initialise the line number
        let lineNumber = 1;

        // Process each line
        for await (const line of rl) {
            if (displayNonEmptyLineNumbers) {
                if (line.trim()) {
                    console.log(`     ${lineNumber++}  ${line}`);
                }
            } else if (displayLineNumbers) {
                console.log(`     ${lineNumber++}  ${line}`);
            } else {
                console.log(line);
            }
        }       
    } catch (error) {
        console.error(`Error reading directory: ${error.message}`);
    }
}

//Get user inputs from command line
const filePaths = program.args;
const displayLineNumbers = program.opts().n;
const displayNonEmptyLineNumbers = program.opts().b;

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
