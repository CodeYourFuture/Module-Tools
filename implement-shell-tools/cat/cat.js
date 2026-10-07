import { program } from "commander";
import { readFile } from "node:fs/promises";

// Set up command options
program
  .name("cat")
  .description("Print file contents")
  .option("-n", "Number all lines")
  .option("-b", "Number non-blank lines only")
  .argument("<files...>", "Files to read")
  .parse();

const options = program.opts();
const files = program.args;

// Process each file
for (const file of files) {
  try {
    const content = await readFile(file, "utf-8");
    const lines = content.split("\n");

    let lineNumber = 1;
    let nonBlankLineNumber = 1;

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];

      // Skip the final empty line that split() creates
      if (i === lines.length - 1 && line === "") break;

      let prefix = "";

      if (options.n) {
        // Number all lines
        prefix = lineNumber.toString().padStart(6) + "  ";
      } else if (options.b && line !== "") {
        // Number only non-blank lines
        prefix = nonBlankLineNumber.toString().padStart(6) + "  ";
      }

      console.log(prefix + line);

      lineNumber++;
      if (line !== "") nonBlankLineNumber++;
    }
  } catch (error) {
    console.error(`Error reading ${file}: ${error.message}`);
  }
}
