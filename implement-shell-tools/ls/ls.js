import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("ls command")
  .description("create ls command")
  .option("-1", "One entry per line")
  .option("-a", "Show all files including hidden")
  .argument("[paths...]", "File paths");

program.parse();

const opts = program.opts();
const paths = program.args.length > 0 ? program.args : ["."];
const onePerLine = opts["1"];
const showAll = opts.a;

for (const targetPath of paths) {
  try {
    let files = await fs.readdir(targetPath);

    if (!showAll) {
      files = files.filter((f) => !f.startsWith("."));
    }

    
    if (paths.length > 1) {
      console.log(`${targetPath}:`);
    }

    if (onePerLine) {
      for (const f of files) console.log(f);
    } else {
      console.log(files.join("  "));
    }

    if (paths.length > 1) {
      console.log(); 
    }
  } catch (err) {
    console.error(`ls: cannot access '${targetPath}': ${err.message}`);
  }
}
