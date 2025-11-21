import process from "node:process";
import {promises as fs} from "node:fs";
import {program} from "commander";

program
    .name("display-file-content")
    .description("Output the content of a file to the terminal")
    .argument("<path>", "The file path to process")
    .option("-n", "Number the output lines")
    .option("-b","Number the non-blank output lines")

program.parse();

const paths = program.args;

const options = program.opts();

const path = paths[0];

const displayFileContent = await fs.readFile(path, "utf-8");

const linesArray = displayFileContent.split("\n");

if (linesArray[linesArray.length - 1] == "") {
    linesArray.pop();
}

const outputLines = [];

let lineNumber = 1;

for (let line in linesArray) {
    if (options.n) {
        const numberedLines = "${lineNumber}  ${line}";
        lineNumber++;
    }
}

