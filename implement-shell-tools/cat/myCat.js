import fs from "node:fs";

const args = process.argv.slice(2);
const files = args;

for (const filename of files) {
  const content = fs.readFileSync(filename, "utf-8");
  process.stdout.write(content);
}
