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

  const numbered = linedText.map((line) => {
    if (numberNonemptyLines) {
      if (line.trim() === "") {
        return line;
      } else {
        return `${String(number++).padStart(3)}  ${line}`;
      }
    }
    if (numberLines) {
      return `${String(number++).padStart(3)}  ${line}`;
    }

    return line;
  });
  console.log(numbered.join("\n"));
}
