import { program } from "commander";

import { promises as fs} from "node:fs";

program
  .name("wc")
  .description("wc implementation")
  .argument("<paths...>", "the file path to process")
  .option("-l", "count how many lines");
program.parse();


const paths = program.args;

if (paths.length === 0) {
  console.error("Expected at least one argument (a path)");
  process.exit(1);
}


const options = program.opts();
const total = {
  linesCounter: 0,
  wordsCounter: 0,
  characterCounter: 0,
};
try {
  for (const path of paths) {
    const content = await fs.readFile(path, "utf-8");

    const linesCounter = content.split("\n").length - 1;
    const wordsCounter = content.trim().split(/\s+/).length;
    const characterCounter = content.length;

    total.linesCounter += linesCounter;
    total.wordsCounter += wordsCounter;
    total.characterCounter += characterCounter;

    if (options.l) {
      console.log(`${linesCounter} ${path}`);
    } else {
      console.log(
        ` ${linesCounter}  ${wordsCounter} ${characterCounter} ${path}`,
      );
    }
  }
  if (paths.length > 1) {
    if (options.l) {
      console.log(`${total.linesCounter} total`);
    } else {
      console.log(
        ` ${total.linesCounter}  ${total.wordsCounter} ${total.characterCounter} total`,
      );
    }
  }
} catch (error) {
  console.error(error.message);
}
