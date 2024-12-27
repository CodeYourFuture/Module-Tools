import { program } from "commander";
import { promises as fs } from "node:fs";

program
    .name("ls")
    .description("list directory contents")
    .option("-1", "Force output to be one entry per line.")
    .option("-a", "Include directory entries whose names begin with a dot (`.`).");

program.parse();
const paths = program.args.length === 0 ? ["."] : program.args;
for (let i = 0; i < paths.length; i++) {
    const path = paths[i];
    const readChildren = await fs.readdir(path);
    const children = [];
    let longest = 0;
    if (program.opts().a) {
        children.push(".", "..");
    }
    for (const child of readChildren) {
        if (program.opts().a || !child.startsWith(".")) {
            children.push(child);
            longest = Math.max(longest, child.length);
        }
    }
    const padTo = longest + (longest % 8 === 0 ? 0 : 8 - (longest % 8));
    if (i > 0) {
        console.log();
    }
    if (paths.length > 1) {
        console.log(`${path}:`);
    }
    if (program.opts()["1"]) {
        console.log(children.join("\n"));
    } else {
        console.log(children.map((child) => child.padEnd(padTo)).join("").trimEnd());
    }
}
