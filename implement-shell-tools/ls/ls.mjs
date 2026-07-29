import process from "node:process";
import { promises as fs } from "node:fs";

const args = process.argv.slice(2);
const flags = args.filter((arg) => arg.startsWith("-"));
const path = args.filter((arg) => !arg.startsWith("-"));
let targetDir = path[0] || ".";
let files = await fs.readdir(targetDir);

if (flags.includes("-a")) {
  files.unshift(".", "..");
} else {
  files = files.filter((fileName) => !fileName.startsWith("."));
}

if (flags.includes("-1")) {
  for (const file of files) {
    console.log(file);
  }
} else {
  console.log(files.join(" "));
}
