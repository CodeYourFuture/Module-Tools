// Import required modules
import { program } from "commander";
import { promises as fs } from "fs";
import * as glob from "glob";

// Set up program
program
    .name("wc command")
    .description("Implementing 'wc' command (-c, -w, -l flags) functionality")
    .argument("<path...>", "Path")
    .option("-c", "Display the number of bytes (characters)")
    .option("-w", "Display the number of words")
    .option("-l", "Display the number of lines")
    .parse(process.argv);

// Function to count bytes, words and lines in a file
async function countDisplayNumBytesWordsLines(filePath, numLines = false, numWords = false, numBytes = false) {
    try {
        // reading file content
        let content = await fs.readFile(filePath, "utf-8");
        // Split content into array by lines
        let arrayLines = content.split("\n");
        
        // Get the number of lines 
        const countNumLines = arrayLines.filter(line => line.trim() !== "").length;
        // Get the number of words using split by any whitespace (spaces, newlines, tabs), filter to remove empty strings
        const countNumWords = content.split(/\s+/).filter(word => word !== "").length;
        // Get the number of bytes (file size in bytes)
        const countNumBytes = (await fs.stat(filePath)).size;

        // Count total of lines, words, bytes
        totalLines += countNumLines;
        totalWords += countNumWords;
        totalBytes += countNumBytes;

        // Formatting output
        const output = [
            numLines || showAll ? countNumLines.toString().padStart(3) : null,
            numWords || showAll ? countNumWords.toString().padStart(3) : null,
            numBytes || showAll ? countNumBytes.toString().padStart(3) : null,
            filePath
        ].filter(element => element !== null).join(" ");
        console.log(output);
    } catch (error) {
        console.error(`Error reading file: ${filePath} - ${error.message}`);
    }
}

// Get command-line arguments
const filePaths = program.args;
const numLines = program.opts().l;
const numWords = program.opts().w;
const numBytes = program.opts().c;

// Show all, if no flags 
const showAll = !numBytes && !numWords && !numLines;

const arrayFilePaths = [];

// Handle "*"
for (const filePath of filePaths) {
    if (filePath.includes("*")) {
        arrayFilePaths.push(...await glob(filePath));
    } else {
        arrayFilePaths.push(filePath);
    }
}

// Initialisation of count total of lines, words, bytes
let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

await Promise.all(arrayFilePaths.map(filePath => countDisplayNumBytesWordsLines(filePath, numLines, numWords, numBytes)));

// Formatting and printing total numbers in console
if (arrayFilePaths.length > 1) {
    console.log(
        [
            numLines || showAll ? totalLines.toString().padStart(3) : null,
            numWords || showAll ? totalWords.toString().padStart(3) : null,
            numBytes || showAll ? totalBytes.toString().padStart(3) : null,
            "total"
        ].filter(element => element !== null).join(" ")
    );
}
