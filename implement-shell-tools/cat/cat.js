import process from "node:process";
import { promises as fs } from "node:fs";

const argv = process.argv.slice(2);
if (argv.length < 1) {
    console.error(`Expected exactly 1 or more arguments (paths) to be passed but got ${argv.length}.`);
    process.exit(1);
}

const stringArr = [];
for (const path of argv) {
    stringArr.push(await fs.readFile(path, "utf-8"));
}

for (let i = 0; i < stringArr.length; i++) {
    console.log(stringArr[i].trim())
}