import process from "node:process";
import { promises as fs, readFile } from "node:fs";

const filesToRead = process.argv.slice(2);
console.log(filesToRead);

async function readMultipleFiles() {
  try {
    const results = await Promise.all(
      filesToRead.map((file) => fs.readFile(file, "utf-8")),
    );
    process.stdout.write(results.join(""));
  } catch (err) {
    console.error("Error reading multiple files:", err);
    process.exitCode = 1;
  }
}

readMultipleFiles();
