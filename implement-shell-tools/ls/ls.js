import process from "node:process";
import { promises as fs } from "node:fs";

const args = process.argv.slice(2);

let showAll = false;
let path = ".";

for (const arg of args) {

  if (arg === "-a") {
    showAll = true;
  }

  else if (arg !== "-1") {
    path = arg;
  }
}

const files = await fs.readdir(path);

for (const file of files) {

  if (!showAll && file.startsWith(".")) {
    continue;
  }

  console.log(file);
}