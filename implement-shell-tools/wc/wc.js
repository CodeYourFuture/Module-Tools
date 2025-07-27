import { program } from "commander";
import { promises as fs } from "node:fs";

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

const opts = program.opts();

const total = [];
const output = [];

const flag_c = (content) => {
  output.push(Buffer.byteLength(content, "utf8"));
};

const flag_w = (content) => {
  output.push(content.match(/\b[\w']+\b/g).length);
};

const flag_l = (content) => {
  output.push(content.split("\n").length - 1);
};

const countAndDisplay = async (path) => {
  const content = await fs.readFile(path, "utf-8");
  output.splice(0);
  if (opts["l"]) {
    flag_l(content);
  }
  if (opts["w"]) {
    flag_w(content);
  }
  if (opts["c"]) {
    flag_c(content);
  }
  if (argv.length > 1) {
    if (total.length == 0) {
      total.push(...output);
    } else {
      for (let index = 0; index < output.length; index++) {
        total[index] += output[index];
      }
    }
  }
  console.log([...output, path].join("     "));
};

const handleInput = async () => {
  if (Object.keys(opts).length == 0) {
    ["l", "w", "c"].forEach((key) => (opts[key] = true));
  }
  for (const path of argv) {
    await countAndDisplay(path);
  }
  if (argv.length > 1) {
    console.log(`${total.join("     ")} total`);
  }
};
handleInput();
