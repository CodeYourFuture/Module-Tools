import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("custom-cat")
  .description("my-own-version-of-cat")
  .option("-n, --line", "Adding a number before each roll")
  .argument("<path>", "The file path to process");

program.parse();

const options = program.opts();

const argv = program.args;
if (argv.length != 1) {
  console.log(`We need exactly 1 path to process but we got ${argv.length}`);
  process.exit(1);
}

const path = argv[0];

const context = await fs.readFile(path, "utf-8");
const contextArray = context.trimEnd().split("\n");
contextArray.forEach((string, index) => {
  options.line
    ? console.log(`     ${index + 1}  ${string}`)
    : console.log(`${string}`);
});
