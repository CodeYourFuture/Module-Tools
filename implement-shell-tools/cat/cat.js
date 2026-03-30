import process from "node:process";
import { promises as fs } from "node:fs";

const argv = process.argv.slice(2);
console.log(argv);

const path = argv[0];

console.log(path);

const content = await fs.readFile(path, "utf-8");
console.log(content.trim());