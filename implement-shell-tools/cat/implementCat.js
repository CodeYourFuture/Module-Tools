import { promises as fs } from "node:fs";
import process from "node:process";

const args = process.argv.slice(2);

if (args.length != 1) {
  console.error(`Expect one argument to be passed but got ${args.length} `);
  process.exit(1);
}

const path = args[0];
const content = await fs.readFile(path, "utf-8");
console.log(content);
