import process from "node:process";
import { promises as fs } from "node:fs";

let args = process.argv.slice(2);
const flags = args.filter((arg) => arg.startsWith("-"));
const filePaths = args.filter((args) => !args.startsWith("-"));
let lineNumber = 1;

for (const filePath of filePaths) {
  const content = await fs.readFile(filePath, "utf-8");

  if (flags.length == 0) {
    process.stdout.write(content);
    continue;
  }

  const lines = content.split("\n");

  for (const line of lines) {
    if (flags.includes("-b")) {
      if (line === "") {
        console.log();
      } else {
        console.log(`${lineNumber}\t${line}`);
        lineNumber++;
      }
    } else if (flags.includes("-n")) {
      console.log(`${lineNumber}\t${line}`);
      lineNumber++;
    }
  }
}
