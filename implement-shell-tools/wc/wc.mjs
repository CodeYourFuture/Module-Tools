import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";
import path from "node:path";

program
  .option("-l", "count lines")
  .option("-w", "count words")
  .option("-c", "count bytes")
  .argument("<files...>", "files to read");

program.action(async (files) => {
  const options = program.opts();

  let totalLines = 0;
  let totalWords = 0;
  let totalBytes = 0;
//helper function
  function formatOutput(lines, words, bytes, label) {
    let output = "";
    if (!options.l && !options.w && !options.c) {
      output += `${lines.toString().padStart(8)} ${words.toString().padStart(8)} ${bytes.toString().padStart(8)}`;
    } else {
      if (options.l) output += lines.toString().padStart(8);
      if (options.w) output += words.toString().padStart(8);
      if (options.c) output += bytes.toString().padStart(8);
    }
    return `${output} ${label}`;
  }

  for (const file of files) {
    try {
      const data = await fs.readFile(file, "utf-8");

      const lines = data.split("\n").length - 1;
      const words = data.trim().split(/\s+/).filter(Boolean).length;
      const bytes = Buffer.byteLength(data, "utf-8");

      totalLines += lines;
      totalWords += words;
      totalBytes += bytes;

      console.log(formatOutput(lines, words, bytes, path.basename(file)));
    } catch (err) {
      console.error(`Error reading ${file}: ${err.message}`);
    }
  }

  if (files.length > 1) {
    console.log(formatOutput(totalLines, totalWords, totalBytes, "total"));
  }
});

program.parse();
