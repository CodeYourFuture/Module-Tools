import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("node-cat")
  .description("A Node.js implementation of the Unix cat command")
  .option("-n, --number", "Number all output lines")
  .option(
    "-b, --numberNonBlank",
    "Numbers only non-empty lines. Overrides -n option"
  )
  .argument("<path...>", "The file path to process");

program.parse();

const paths = program.args;
const { number, numberNonBlank } = program.opts();

console.log(number, numberNonBlank);

let content = "",
  output;

for (const path of paths) {
  content += await fs.readFile(path, "utf-8");
}

output = content.trim();

if (numberNonBlank) {
  const outputArr = output.split("\n");
  let lineCounter = 1;
  for (let i = 0; i < outputArr.length; i++) {
    if (outputArr[i].trim() === "") continue;
    outputArr[i] = `${String(lineCounter++).padStart(6, " ")}  ${outputArr[i]}`;
  }
  console.log(outputArr.join("\n"));
} else if (number) {
  const outputArr = output.split("\n");
  for (let i = 0; i < outputArr.length; i++) {
    outputArr[i] = `${String(i + 1).padStart(6, " ")}  ${outputArr[i]}`;
  }
  console.log(outputArr.join("\n"));
} else {
  console.log(output);
}
