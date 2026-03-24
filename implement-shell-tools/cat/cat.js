import process from "node:process";
import { promises as fs } from "node:fs";

const argv = process.argv.slice(2);
if (argv.length < 1) {
    console.error(`Expected exactly 1 or more arguments (paths) to be passed but got ${argv.length}.`);
    process.exit(1);
}
const paths = argv;

for (const path of paths) {
    console.log(await fs.readFile(path, "utf-8"));
}
