import { program } from "commander";
import { error } from "node:console";
import { promises as fs } from "node:fs";

program
  .name("cat")
  .description("cat sample-files/1.txt ")
  .argument("<path>", "The file path to process");
program.parse();

const argv = program.args;
if (argv.length != 1) {
  console.error(
    `Expected exactly 1 argument (a path) to  be passed but got ${argv.length}`,
  );
  process.exit(1);
}
const path = argv[0];
try {
  const content = await fs.readFile(path, "utf-8");
  process.stdout.write(content);
} catch (error) {
  console.error(error.message);
  process.exit(1);
}
