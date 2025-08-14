import fs from "fs/promises"; // Import fs.promises for async file reading
import { Command } from "commander";

const program = new Command();

program
  .command("readfiles <files...>") // Accepts multiple file arguments
  .description("read text files")
  .option("-n, --number", "show line number")
  .option("-b, --non-blank", "number 'only' the non-blank lines")
  .action(async (files, options) => {
    let lineCounter = 1; // Continuous line number for `-n`
    let nonBlankCounter = 1; // Non-blank line number for `-b`

    for (const file of files) {
      try {
        // Read file content using promises (async/await)
        const data = await fs.readFile(file, "utf8");
        let lines = data.split("\n");

        if (options.number) {
          lines = lines.map((line) => `${lineCounter++} ${line}`);
        } else if (options.nonBlank) {
          lines = lines.map((line) =>
            line.trim() === "" ? line : `${nonBlankCounter++} ${line}`
          );
        }
        console.log(lines.join("\n"));
      } catch (err) {
        console.error(err);
      }
    }
  });

program.parse();
