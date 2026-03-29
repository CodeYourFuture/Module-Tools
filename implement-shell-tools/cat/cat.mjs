import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("cat")
  .description("cat sample-files/1.txt ")
  .option("-n", "number all lines")
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

  const addLineNumber = program.opts();
  if (addLineNumber.n) {
    const lines = content.split("\n");

    if (lines[lines.length - 1] === "") {
      lines.pop();
    }
    
    lines.forEach((line, index) => {
      process.stdout.write(`${index + 1} ${line}\n`);
    });
  } else process.stdout.write(content);
} catch (error) {
  console.error(error.message);
  process.exit(1);
}
