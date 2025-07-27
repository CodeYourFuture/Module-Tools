import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("count-containing-words")
  .description("Counts words in a file that contain a particular character")
  .option(
    "-l",
    "The number of lines in each input file is written to the standard output."
  )
  .option(
    "-w",
    "The number of words in each input file is written to the standard output."
  )
  .option(
    "-c",
    "The number of bytes in each input file is written to the standard output."
  )
  .argument("<path...>", "The file path to process")
  .parse();

const argv = program.args;
console.log(argv);

const opts = program.opts();
console.log("OPTS", opts);

const total = [0, 0, 0];

const flag_l = (content) => {
  return Buffer.byteLength(content, "utf8");
};

const flag_w = (content) => {
  return content.match(/\b[\w']+\b/g).length;
};

const flag_c = (content) => {
  return content.split("\n").length - 1;
};

const countAndDisplay = async (path) => {
  const content = await fs.readFile(path, "utf-8");
  if (opts["l"]) {
    const countOfLines = flag_c(content);
    total[0] += countOfLines;
    return countOfLines;
  }
  const countOfWords = flag_w(content);
  total[1] += countOfWords;
  const countOfBytes = flag_l(content);
  total[2] += countOfBytes;
  console.log([countOfLines, countOfWords, countOfBytes, path].join("     "));
};

const handleInput = async () => {
  for (const path of argv) {
    await countAndDisplay(path);
  }
  if (argv.length > 1) {
    console.log(`${total.join("     ")} total`);
  }
};
handleInput();
