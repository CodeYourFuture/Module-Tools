import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

// configure the CLI program with its name, description, arguments, options, and actions (the help instructions)
program
    .name("cat")
    .description("An alternative to the 'cat' command")
    .argument("<files...>", "The file(s) to process") 
    .option("-n, --number", "Number all output lines")
    .option("-b, --number-nonblank", "Number non-blank output lines")
    // actions to process the provided files with the specified options (-n, -b)
    .action(async (files, options) => {
        try {
            // call newCat for all files
            await newCat(files, options.number, options.numberNonblank)
        } catch (err) {
        console.error(`Error: ${err.message}`);
        }
  });

// parse command-line file arguments using the process.argv array
program.parse(process.argv);


async function newCat(files, numberLines, numberNonBlank) {
    let lineNumber = 1;

    for (const file of files) {
        // read each file into a single text string
        try {
            const data = await fs.readFile(file, "utf8");
            // split that string into an array at \n where each element is a line from the file
            // e.g. lines = ["Line 1", "Line 2", "Line 3"]
            const lines = data.split("\n")

            // remove trailing blank line caused by a trailing newline
            if (lines[lines.length - 1] === "") {
                lines.pop();
            }

            for (const line of lines) {
                if (numberNonBlank) {
                    // check what is left on the line after trimming (truthy = text, falsy = blank)
                    if (line.trim()) {
                    console.log(`${lineNumber.toString().padStart(6, ' ')}  ${line}`);
                    lineNumber++   
                    }  else {
                        console.log(line)
                    } 
                } else if (numberLines) {
                    // number all lines
                    console.log(`${lineNumber.toString().padStart(6, ' ')}  ${line}`);
                    lineNumber++
                } else {
                    // if neither flag print normally
                    console.log(line)
                }
            }
        } catch (err) {
              console.error(`Error reading file ${file}: ${err.message}`);
        }
    }
}