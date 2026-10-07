import { readFile } from "node:fs/promises";
import process from "node:process";
import { parseArgs } from "node:util";

const { values, positionals: files } = parseArgs({
  args: process.argv.slice(2),
  options: {
    number: {
      type: "boolean",
      short: "n",
    },
    numberNonBlank: {
      type: "boolean",
      short: "b",
    },
  },
  allowPositionals: true,
});

const showLineNumbers = values.number ?? false;
const numberNonBlankLines = values.numberNonBlank ?? false;

let lineNumber = 1;

for (const file of files) {
  try {
    const content = await readFile(file, "utf-8");
    
    const lines = content.split("\n");

    if (numberNonBlankLines) {
      for (const line of lines) {
        if (line !== "") {
          console.log(`${lineNumber} ${line}`);
          lineNumber++;
        } else {
          console.log("");
        }
      }
    } else if (showLineNumbers) {
      for (const line of lines) {
        console.log(`${lineNumber} ${line}`);
        lineNumber++;
      }
    } else {
      process.stdout.write(content);
    }
  } catch (err) {
    console.error(err.message);
  }
}