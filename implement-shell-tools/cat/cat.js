import process from "node:process";
import { promises as fs } from "node:fs";

const args = process.argv.slice(2);

let option = "none";
const paths = [];


for (const arg of args) {
  if (arg === "-n") {
    option = "n";
  } else if (arg === "-b") {
    option = "b";
  } else {
    paths.push(arg);
  }
}

if (paths.length === 0) {
  console.error("Expected at least one file path.");
  process.exit(1);
}

for (const path of paths) {
  const content = await fs.readFile(path, "utf-8");

  const lines = content.split("\n");

  let lineNumber = 1;

  for (const line of lines) {

    if (option === "n") {
      console.log(`${lineNumber} ${line}`);
      lineNumber++;
    }

    else if (option === "b") {

      if (line !== "") {
        console.log(`${lineNumber} ${line}`);
        lineNumber++;
      } else {
        console.log("");
      }

    }

    else {
      console.log(line);
    }
  }
}