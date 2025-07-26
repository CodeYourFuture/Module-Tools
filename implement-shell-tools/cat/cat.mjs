import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
    .name("display-content-of-a-file")
    .description("cat is used to display the content of a file or print the content of a file.")
    .argument("<path>", "The file path to process");


program.action(async (path) => {
    const data = await fs.readFile(path, "utf-8");
    process.stdout.write(data);
});
program.parse();