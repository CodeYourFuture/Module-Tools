import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("Custom-ls")
  .description("Custom-ls-that-works-like-ls")
  .option("-1, --oneFile", "Showing one file per line")
  .option("-a, --showHidden", "Showing hidden files")
  .argument("[path]", "The file path to process");

program.parse();

const argumentsArray = program.args;

const path = argumentsArray[0] || "./";

try {
  const files = await fs.readdir(path);

  const sortedFiles = files.sort((a, b) => a.localeCompare(b));

  const options = program.opts();

  let renderingFiles = [];

  if (options.showHidden) {
    renderingFiles = sortedFiles;
  } else {
    renderingFiles = sortedFiles.filter((file) => !/^\./.test(file));
  }

  if (options.oneFile) {
    for (let file of renderingFiles) {
      console.log(file);
    }
  } else {
    console.log(renderingFiles.join(" "));
  }
} catch (error) {
  const state = await fs.stat(path).catch(() => null);
  if (state && state.isFile()) {
    console.log(path);
  } else {
    console.log(
      `Can't access to this path: ${path} - No such file or directory`,
    );
    process.exit(1);
  }
}
