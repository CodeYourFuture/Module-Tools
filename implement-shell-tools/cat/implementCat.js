import { promises as fs, readFile } from "node:fs";
import process from "node:process";

let filePaths = process.argv.slice(2);

async function readFiles(paths) {
  try {
    const promises = paths.map((filePath) => fs.readFile(filePath, "utf-8"));
    const contents = await Promise.all(promises);
    return contents;
  } catch (err) {
    console.error(err.message);
  }
}

async function displayFileContents() {
  const contents = await readFiles(filePaths);
  contents.forEach((content) => console.log(content));
}

await displayFileContents();
