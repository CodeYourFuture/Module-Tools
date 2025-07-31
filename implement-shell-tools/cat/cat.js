import { program } from "commander";
import process from "node:process";
import { promises as fs } from "node:fs";

program
  .name("cat")
  .description("Prints file contents to the terminal")
  .option("-n", "number all output lines")
  .argument("<files...>", "Files to print");

program.parse();

const files = program.args;

if (files.length < 1) {
  console.error("Please specify one or more files.");
  process.exit(1);
}

async function printFileContent(filename) {
  try {
    const content = await fs.readFile(filename, "utf-8");
    process.stdout.write(content);
  } catch {
    console.error(`Could not read file: ${filename}`);
  }
}

(async () => {
  for (const file of files) {
    await printFileContent(file);
  }
})();
