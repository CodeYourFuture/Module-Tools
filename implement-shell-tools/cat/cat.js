import process from "node:process";
import { promises as fs } from "node:fs";

const args = process.argv.slice(2);

let showNumbers = false;
const paths = [];

for (const arg of args) {
  if (arg === "-n") {
    showNumbers = true;
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

  if (showNumbers) {
    let i = 1;

    for (const line of lines) {
      console.log(`${i} ${line}`);
      i++;
    }

  } else {
    console.log(content);
  }
}