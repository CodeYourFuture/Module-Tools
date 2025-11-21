import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("count-containing-words")
  .description("Counts words in a file that contain a particular character, optionally gives word or character counts.")
  .option("-c, --char <char>", "The character to search for", "e")
  .option("-n, --count [type]", "Count type: words or chars")
  .argument("<path>", "The file path to process");

program.parse();

const argv = program.args;
if (argv.length != 1) {
  console.error(
    `Expected exactly 1 argument (a path) to be passed but got ${argv.length}.`
  );
  process.exit(1);
}

const path = argv[0];
// const { char, count } = program.opts();
console.log(path);

const content = await fs.readFile(path, "utf-8");

const countOfWordsContainingChar = content
  .split(/\s+/)
  .filter((word) => word.includes(char)).length;

if (count) {
  if (count === "words") {
    const countOfWords = content.split(" ").length;
    console.log(countOfWordsContainingChar, countOfWords);
  } else if (count === "chars") {
    const countOfChars = content.length;
    console.log(countOfWordsContainingChar, countOfChars);
  }
} else {
  console.log(countOfWordsContainingChar);
}
