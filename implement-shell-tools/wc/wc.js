import process from "node:process";
import { promises as fs } from "node:fs";

const args = process.argv.slice(2);

if (args.length === 0) {
  console.error("Please provide at least one file");
  process.exit(1);
}

for (const path of args) {
  const content = await fs.readFile(path, "utf-8");

  const lines = content.split("\n").length;
  const words = content.split(" ").length;
  const chars = content.length;

  console.log(lines, words, chars, path);
}