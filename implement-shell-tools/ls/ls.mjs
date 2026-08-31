import process from "node:process";
import { promises as fs } from "node:fs";
import { program } from "commander";

program
  .name("list")
  .description("Implement my version of ls")
  .argument("[paths...]", "The file path to process")
  .option("-1, --one", "This list the item one per line")
  .option("-a, --all", "This lists all of the files");

program.parse();

const { one, all } = program.opts();
const paths = program.args;

let targetDir = paths[0] || ".";

try {
  let files = await fs.readdir(targetDir);

  if (all) {
    files = [".", "..", ...files].sort();
  } else {
    files = files.filter((output) => !output.startsWith(".")).sort();
  }

  if (one) {
    for (const file of files) {
      console.log(file);
    }
  } else {
    console.log(files.join(" "));
  }
} catch (error) {
  console.error(`${error}`);
}
