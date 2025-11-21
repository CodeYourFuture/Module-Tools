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

const lines = displayFileContent.split("\n");

process.stdout.write(displayFileContent);

