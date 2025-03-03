import { promises as fs, readFile } from "node:fs";
import process from "node:process";

const args = process.argv.slice(2);

// if (args.length != 1) {
//   console.error(`Expect one argument to be passed but got ${args.length} `);
//   process.exit(1);
// }

async function readFiles(paths) {
  try {
    const promises = paths.map((filePath) => fs.readFile(filePath, "utf-8"));
    const contents = await Promise.all(promises);
    return contents;
  } catch (err) {
    console.error(err.message);
  }
}

