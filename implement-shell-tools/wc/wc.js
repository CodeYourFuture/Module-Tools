import fs from "fs/promises";
import { Command } from "commander";

const program = new Command(); //Creates a new instance of the Command class, which will handle our command-line arguments and commands.

// Write a function to count lines, words and bytes

async function count(file, options) {
  const data = await fs.readFile(file, "utf8");

  const linesCount = data.split("\n").length;

  const wordsCount = data.split(/\s+/).filter(Boolean).length;

  const bytes = Buffer.byteLength(data, "utf8");

  let output = `${file}:`; //creates a string variable that will be used to store and build the final string that will be printed to the console.

  if (options.lines) {
    output += ` ${linesCount}`;
    console.log(output);
  }
  if (options.words) {
    output += ` ${wordsCount}`;
    console.log(output);
  }

  if (options.bytes) {
    output += `${bytes}`;
    console.log(output);
  }

  // If no options were provided, show all counts
  if (!options.lines && !options.words && !options.bytes) {
    output += ` ${linesCount} ${wordsCount} ${bytes}`;
    console.log(output);
  }
}

program
  .command("wc <files...>") //The <files...> syntax means it accepts one or more file names as arguments.
  .description("Count lines, words, and bytes in text files")
  .option("-l, --lines", "Count lines")
  .option("-w, --words", "Count words")
  .option("-c, --bytes", "Count bytes")
  .action(async (files, options) => {
    for (const file of files) {
      await count(file, options);
    }
  });

program.parse();
