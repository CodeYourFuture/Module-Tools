import { promises as fs } from "node:fs";
import process from "node:process";
import { program } from "commander";

program
    .name("Implement cat")
    .description("Implement a version of the cat program")
    .option("-n, --number", "Number the output lines, starting at 1")
    .argument("<paths...>", "The file paths to process")
    .parse(process.argv);

let filePaths = program.args;

async function readFiles(paths) {
    try {
        const promises = paths.map((filePath) => fs.readFile(filePath, "utf-8"));
        const contents = await Promise.all(promises);
        return contents;
    } catch (err) {
        console.error(err.message);
    }
}

async function displayFileContents() {
    const contents = await readFiles(filePaths);
    const numberLines = program.opts().number;

    contents.forEach((content) => {
        if (numberLines) {
            content.split('\n').forEach((line, lineNumber) => {
                console.log(`${lineNumber + 1} ${line}`);
            });
        } else {
            console.log(content);
        }
    });
}

await displayFileContents();
