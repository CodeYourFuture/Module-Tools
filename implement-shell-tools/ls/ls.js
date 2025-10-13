import { program } from "commander";
import { readdir } from "node:fs/promises";

program
  .name("ls")
  .description("List directory contents")
  .option("-1", "One entry per line")
  .option("-a", "Show hidden files")
  .argument("[dir]", "Directory to list", ".")
  .parse();

const options = program.opts();
const dir = program.args[0] || ".";

try {
  const files = await readdir(dir);

  // Add . and .. if using -a
  let allFiles = options.a ? [".", ".."] : [];

  // Add regular files (filter hidden unless -a is used)
  for (const file of files) {
    if (options.a || !file.startsWith(".")) {
      allFiles.push(file);
    }
  }

  // Output
  if (options["1"]) {
    allFiles.forEach(console.log);
  } else {
    console.log(allFiles.join(" "));
  }
} catch (err) {
  console.error(`ls: ${dir}: ${err.message}`);
}
