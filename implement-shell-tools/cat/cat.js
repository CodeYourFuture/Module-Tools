import process from "node:process";
import {promises as fs} from "node:fs";
import {program} from "commander";

program
    .name("display-file-content")
    .description("Output the content of a file to the terminal")
    .argument("<path>", "The file path to process")
    .option("-n", "Number the output lines")

program.parse();

const paths = program.args;

const options = program.opts();

const path = paths[0];

const displayFileContent = await fs.readFile(path, "utf-8");

const linesArray = displayFileContent.split("\n");

if (linesArray[linesArray.length - 1] == "") {
    linesArray.pop();
}

const numberedLinesArray = linesArray.map((line, index) => `${index + 1}  ${line}`);

const numberedLines = numberedLinesArray.join("\n")

if (options.n) {
    process.stdout.write(numberedLines);
} else {
    process.stdout.write(displayFileContent);
}



