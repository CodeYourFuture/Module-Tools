import process from "node:process";
import { promises as fs } from "node:fs";

const args = process.argv.slice(2);

let option = "all";
const paths = [];

// parse args
for (const arg of args) {
  if (arg === "-l") option = "l";
  else if (arg === "-w") option = "w";
  else if (arg === "-c") option = "c";
  else paths.push(arg);
}

if (paths.length === 0) {
  console.error("Please provide at least one file");
  process.exit(1);
}

for (const path of paths) {
  const content = await fs.readFile(path, "utf-8");

  const lines = content.split("\n").length;
  const words = content.split(" ").length;
  const chars = content.length;

  if (option === "l") {
    console.log(lines, path);
  } else if (option === "w") {
    console.log(words, path);
  } else if (option === "c") {
    console.log(chars, path);
  } else {
    console.log(lines, words, chars, path);
  }
}