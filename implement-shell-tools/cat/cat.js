import process from "node:process";
import { promises as fs } from "node:fs";

const arrArgv = process.argv.slice(2);

const numberLines = arrArgv.includes("-n");
const numberNonemptyLines = arrArgv.includes("-b");

const nonFlagArrArgv = arrArgv.filter((arr) => !arr.startsWith("-"));

let number = 1;

for (let file of nonFlagArrArgv) {
  const content = await fs.readFile(file, "utf-8");

  const linedText = content.split("\n");

  const formatLines = (line) => {
    return `${String(number++).padStart(3)}  ${line}`;
  };

  const numbered = linedText.map((line) => {
    if (numberNonemptyLines && line.trim() === "") {
      return line;
    }
    if (numberNonemptyLines || numberLines) {
      return formatLines(line);
    }
    return line;
  });
  console.log(numbered.join("\n"));
}
