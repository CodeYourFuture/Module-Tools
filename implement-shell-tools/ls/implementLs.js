import process from "node:process";
import { promises as fs } from "node:fs";
import { program } from "commander";

program
    .name("Implement ls")
    .description("Implements a version of the ls command")
    .option("-1, --one", "Output all files and directories each in a line")
    .parse(process.argv);

const filePaths = program.args.length ? program.args : ['.'];
const one = program.opts().one;

filePaths.forEach(async (filePath) => {
    try {
        const files = await fs.readdir(filePath);
        if (one) {
            files.forEach(file => console.log(file));
        } else {
            console.log(files.join(' '));
        }
    } catch (err) {
        console.error(`Error reading directory ${filePath}:`, err.message);
    }
});
