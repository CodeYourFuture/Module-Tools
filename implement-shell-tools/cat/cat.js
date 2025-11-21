import process from "node:process";
import {promises as fs} from "node:fs";
import {program} from "commander";


const argv = process.argv.slice(2);
if (argv.length != 1) {
    console.error("Expected exactly 1 argument or a path but received ${argv.length.");
    process.exit(1);
}

const path = argv[0];

const displayFileContent = await fs.readFile(path, "utf-8");

process.stdout.write(displayFileContent);

