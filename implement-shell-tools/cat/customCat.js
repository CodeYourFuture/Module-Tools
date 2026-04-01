#!/usr/bin/env node
import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("ccat")
  .description("CLI command to concatenate and print files")
  .option("-n, --number", "Number all output lines starting, at 1")
  .option("-b, --nonBlank", "Number only non-blank lines, starting at 1")
  .argument("<files...>", "Files to read");

program.parse();

const argv = program.args;
const options = program.opts();

for (const filePath of argv) {
  try {
    const content = await fs.readFile(filePath, "utf-8");
    const lines = content.split("\n");

    if (lines[lines.length - 1] === "") lines.pop();

    lines.forEach((line, index) => {
      if (options.nonBlank) {
        if (line.trim() !== "") {
          process.stdout.write(
            `${(index + 1).toString().padStart(6)} ${line}\n`,
          );
        } else process.stdout.write(`${line}\n`);
      } else if (options.number) {
        process.stdout.write(`${(index + 1).toString().padStart(6)} ${line}\n`);
      } else {
        process.stdout.write(`${line}\n`);
      }
    });
  } catch (error) {
    console.error(`ccat: ${filePath}: No such file or directory.`);
  }
}
