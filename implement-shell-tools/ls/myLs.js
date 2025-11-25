import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("myLs")
  .description("my ls clone")
  .option("-1", "one entry per line")
  .option("-a", "show hidden files")
  .argument("[paths...]", "file or directory paths");

program.parse();

const opts = program.opts();
let paths = program.args;

if (paths.length === 0) {
  paths = ["."];
}

for (const path of paths) {
  const entries = await fs.readdir(path);

  for (const file of entries) {
    if (!opts.a && file.startsWith(".")) {
      continue;
    }

    if (opts["1"]) {
      console.log(file);
    } else {
      console.log(file + " ");
    }
  }

}
