import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("custom-cat")
  .description("my-own-version-of-cat")
  .option("-n, --line", "Adding a number before each roll")
  .option(
    "-b, --nonBlank",
    "Only adding a number before roll that is non blank",
  )
  .argument("<path...>", "The file path to process");

program.parse();

const options = program.opts();

const argv = program.args;
if (argv.length < 1) {
  console.log(
    `We need at least 1 path of file to process but we got ${argv.length}`,
  );
  process.exit(1);
}

const paths = argv;

let count = 1;

for (let path of paths) {
  const context = await fs.readFile(path, "utf-8");
  if (options.line && options.nonBlank) {
    context
      .trimEnd()
      .split("\n")
      .forEach((string) => {
        if (string != null || string != "") {
          console.log(`     ${count}  ${string}`);
          count++;
        } else {
          console.log(string);
        }
      });
  } else {
    console.log(context.trimEnd());
  }
}
