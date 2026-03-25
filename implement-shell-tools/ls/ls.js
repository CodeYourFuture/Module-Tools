import { program } from "commander";
import process from 'node:process';
import fs from 'node:fs';

let vertical = false;

program.name("list-directory-contents").description("Shows all files and folders in a directory").option("-1", "List one file/directory per line").argument("[path]", "Path of the directory to list (defaults to .)")

program.parse();

const argv = program.args;

vertical = program.opts()[1]

const folderPath = argv[0] || ".";

const contents = fs.readdirSync(folderPath);

if (!vertical) {
    console.log(contents.join("  "));
} else {
    for (const content of contents) {
        console.log(content);
    }
}