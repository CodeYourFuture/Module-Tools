import process from "node:process";
import {promises as fs} from "node:fs";
import {program} from "commander";

program
    .name("display-file-content")
    .description("Output the content of a file to the terminal")
    .argument("<path>", "The file path to process")
    .option("-n", "Number the output lines")

program.parse();

const argv = program.args;
if (argv.length != 1) {
    console.error("Expected exactly 1 argument or a path but received ${argv.length.");
    process.exit(1);
}

const path = argv[0];
const options = program.opts();


const displayFileContent = await fs.readFile(path, "utf-8");

process.stdout.write(displayFileContent);

