import { promises as fs } from "node:fs";
import process from "node:process";
import { program } from "commander";

program
  .name("Implement cat")
  .description("Implement a version of the cat program")
  .option("-n, --number", "Number the output lines, starting at 1")
  .argument("<paths...>", "The file paths to process")
  .parse(process.argv);

let filePaths = program.args;

async function readFiles(paths) {
  try {
    const promises = paths.map((filePath) => fs.readFile(filePath, "utf-8"));
    const contents = await Promise.all(promises);
    return contents.map((content) => {
      return extractLinesFromContent(content);
    });
  } catch (err) {
    console.error(err.message);
  }
}

function extractLinesFromContent(content) {
    const lines = content.split("\n");
    if (lines[lines.length - 1] === "") {
        lines.pop(); // excludes last line if it empty
    }
    return lines;
}

async function displayFileContents() {
  const contents = await readFiles(filePaths);
  const flatternedContents = contents.flat();
  const numberLines = program.opts().number;

  flatternedContents.forEach((line, index) => {
    if (numberLines) {
      console.log(`${index + 1} ${line}`);
    } else {
      console.log(line);
    }
  });
}

await displayFileContents();
