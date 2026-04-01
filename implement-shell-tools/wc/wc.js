import { promises as fs } from "node:fs";
import { program } from "commander";
import { get } from "node:http";

program
  .name("print newline, word, and byte counts for each file")
  .option("-a", "to do something")
  .argument("<paths...>", "file name");

program.parse();

const paths = program.args;

async function getNoFlagsOutput(paths) {
  let lineCountTotal = 0;
  let wordCountTotal = 0;
  let fileSizeTotal = 0;
  let output = [];

  for (const filename of paths) {
    try {
      const file = await fs.stat(filename);

      if (file.isFile()) {
        const fileContent = await fs.readFile(filename, "utf-8");
        const lineCount = fileContent.match(/\n/g).length;
        const wordCount = fileContent
          .trim()
          .split(/\s+/)
          .filter(Boolean).length;
        const fileSize = file.size;

        output.push([lineCount, wordCount, fileSize, filename]);
      }
    } catch (err) {
      output.push([filename, `wc: ${filename} ${err.message}`]);
    }
  }

  return output;
}
//console.log(`${lineCountTotal} ${wordCountTotal} ${fileSizeTotal}Total`);
console.log(JSON.stringify(await getNoFlagsOutput(paths)));
