// Getting the 'promises' part of the 'fs' module and calling it 'fs' to make it easier to use
import { promises as fs } from "fs";
// Getting the 'resolve' function from 'path' module to turn relative path (from argument) into full path (absolute path)
import { resolve } from "path";
// Importing the 'program' object from 'commander' to help build command-line interfaces, handle user inputs.
import { program } from "commander";
// Importing the 'chalk' module to add colors and styles to text in the console
import chalk from "chalk";

// Function to list contents of a directory. 
async function listDirectoryFiles(directoryPath, showHiddenFiles = false, oneFilePerLine = false) {
    try {
        // Function call from the fs module. It reads contents of a directory, returns an array of file names (files)
        let files = await fs.readdir(directoryPath);
        // Array stores current directory, parent directory)
        let dotDirectories = [];
        // Array stores the names of the files and directories
        let displayFiles = [];
        // Ensure '.', '..' are on the top of list when we list hidden files
        if (showHiddenFiles) {
            dotDirectories = [".", ".."];
        }
        // Loop through files and add to displayFiles, including hidden files if -a flag is set
        for (const file of files) {            
            if (!file.startsWith(".") || showHiddenFiles) {
                displayFiles.push(file);
            }
        }
        // Sort files without leading dots for hidden files
        displayFiles.sort((a, b) => {
            const fileNameA = a.startsWith(".") ? a.slice(1) : a;
            const fileNameB = b.startsWith(".") ? b.slice(1) : b;
            // Compares two filenames, considering numbers and ignoring case sensitivity
            return fileNameA.localeCompare(fileNameB, "en", { numeric: true, sensitivity: "base" });
        });
        // Merging two arrays into one
        let sortedFiles = [...dotDirectories, ...displayFiles];

        const allFiles = sortedFiles.map(file => {
            // Creating the absolute path for the file by combining directoryPath and file name
            const absoluteFilePath = resolve(directoryPath, file);
            // Check if the file is a directory; if yes, color it blue, otherwise keep it normal.
            return fs.stat(absoluteFilePath).then(stats =>
                stats.isDirectory() ? chalk.blue.bold(file) : file
            );
        });
        // Array with style directory in bold and blue
        const styledAllFiles = await Promise.all(allFiles);
        // Print files either one per line or in a single line separated by spaces
        console.log(oneFilePerLine ? styledAllFiles.join("\n") : styledAllFiles.join("  "));
        // If an error occurs while reading the directory, console the error message
    } catch (error) {
        console.error(`Error reading directory: ${error.message}`);
    }
}
// Configure the CLI tool with name, description, arguments, and options
// 'program' is from the Commander package and handles command-line arguments
program
    .name("ls command")
    .description("Implementing ls command (-1, -a flags) functionality")
    .argument("[path]", "Path to list", ".")
    .option("-a", "List hidden files, directories")
    .option("-1", "List one file, directory per line")
    // Read and process command-line arguments, process.argv - an array containing the command-line arguments
    .parse(process.argv);

// Get user inputs from command-line options and arguments
const directory = program.args[0] || ".";
const showHiddenFiles = program.opts().a;
const oneFilePerLine = program.opts()["1"];

// Resolve the absolute path of the directory
const absoluteDirectoryPath = resolve(directory);
// Call the function to list the files in the directory (with options)
await listDirectoryFiles(absoluteDirectoryPath, showHiddenFiles, oneFilePerLine);