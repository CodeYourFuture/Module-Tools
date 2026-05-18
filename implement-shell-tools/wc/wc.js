import process from "node:process";
import { promises as fs } from "node:fs";

const args = process.argv.slice(2);

const path = args[0];

if (!path) {
  console.error("Please provide a file path");
  process.exit(1);
}

const content = await fs.readFile(path, "utf-8");

const lines = content.split("\n").length;
const words = content.split(" ").length;
const chars = content.length;

console.log(lines, words, chars);