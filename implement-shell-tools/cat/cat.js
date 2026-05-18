import process from "node:process";
import { promises as fs } from "node:fs";

const paths = process.argv.slice(2);

if (paths.length === 0) {
  console.error("Expected at least one file path.");
  process.exit(1);
}

for (const path of paths) {
  const content = await fs.readFile(path, "utf-8");
  console.log(content);
}