import { program } from "commander";
import { promises as fs } from "node:fs";


program
  .name("cat")
  .description("Prints file content with optional line numbers")
  .argument("<file>", "file to read")
  .option("-n, --number", "number all lines")
  .option("-b, --number-nonblank", "number non-blank lines only")
  .parse();

const options = program.opts();
const filePath = program.args[0];

try {
  const content = await fs.readFile(filePath, "utf-8");
  const lines = content.split("\n");

  lines.forEach((line, index) => {
    const lineNumber = index + 1;
    if (options.number) {
    
      console.log(`${lineNumber.toString().padStart(4)}  ${line}`);
    } else if (options.numberNonblank) {
      
      if (line.trim() === "") {
        console.log("     " + line);
      } else {
        console.log(`${lineNumber.toString().padStart(4)}  ${line}`);
      }
    } else {

      console.log(line);
    }
  });
} catch (err) {
  console.error(`Error reading file "${filePath}":`, err.message);
  process.exit(1);
}

   

