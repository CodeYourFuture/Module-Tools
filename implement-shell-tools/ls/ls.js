import process from "node:process";
import { promises as fs } from "node:fs";

const args = process.argv.slice(2);

let path = ".";

if (args[1]) {
  path = args[1];
}

const files = await fs.readdir(path);

for (const file of files) {
  console.log(file);
}