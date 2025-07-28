import { promises as fs } from "node:fs";
// import path from "node:path";
import { program } from "commander";
import { clearLine } from "node:readline";

program
  .name("cat")
  .description("Concatenate and print files")
  .option("-n", "Number the output lines, starting at 1")
  .option("-b", "Number the non-blank output lines, starting at 1")
  .argument("<sample-files...>", "The file path to process")
  .parse();

const argv = program.args;

const opts = program.opts();

const flag_n = (data) => {
  const numberOfLines = data.split("\n").length - 1;
  return numberOfLines;
};
let number = 0;
async function example(path) {
  try {
    const data = await fs.readFile(path, { encoding: "utf8" });
    if (opts["n"]) {
      const lines = data.split("\n");
      if (lines[lines.length - 1] === "") {
        lines.pop();
      }

      for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        const output = `${number + 1} ${line}`;
        number += 1;
        console.log(output.trimEnd());
      }
    } else {
      console.log(data.trimEnd());
    }
  } catch (err) {
    console.error(err);
  }
}

const handleInput = async () => {
  for (const path of argv) {
    await example(path);
  }
};

handleInput();
// for (const path of argv) {
//   example(path);
// }
