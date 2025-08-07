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
  const options = program.opts(); // get the options the user used

  let totalLines = 0;
  let totalWords = 0;
  let totalBytes = 0;

  for (const file of files) {
    try {
      const data = await fs.readFile(file, "utf-8"); // read file content

      //count lines,words and bytes
      const lines = data.split("\n").length - 1;
      const words = data.trim().split(/\s+/).filter(Boolean).length;
      const bytes = Buffer.byteLength(data, "utf-8");

      totalLines += lines;
      totalWords += words;
      totalBytes += bytes;

      const filename = path.basename(file);

      // prepare line to show
      let output = "";
      if (!options.l && !options.w && !options.c) {
        //if no flag is used, show all
        output += `${lines.toString().padStart(8)} ${words.toString().padStart(8)} ${bytes.toString().padStart(8)} ${filename}`;
      } else {
        if (options.l) output += lines.toString().padStart(8);
        if (options.w) output += words.toString().padStart(8);
        if (options.c) output += bytes.toString().padStart(8);
        output += ` ${filename}`;
      }

      console.log(output);

    } catch (err) {
      console.error(`Error reading ${file}: ${err.message}`);
    }
  }

  //If more than one file, show total
  if (files.length > 1) {
    let totalOutput = "";
    if (!options.l && !options.w && !options.c) {
      totalOutput += `${totalLines.toString().padStart(8)} ${totalWords.toString().padStart(8)} ${totalBytes.toString().padStart(8)} total`;
    } else {
      if (options.l) totalOutput += totalLines.toString().padStart(8);
      if (options.w) totalOutput += totalWords.toString().padStart(8);
      if (options.c) totalOutput += totalBytes.toString().padStart(8);
      totalOutput += " total";
    }
    console.log(totalOutput);
  }
});

program.parse(); //start the command
