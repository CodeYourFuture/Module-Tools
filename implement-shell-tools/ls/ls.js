import {program} from "commander";
import {promises as fs} from "node:fs";

program
 .name ("ls")
 .description("List the file directory")
 .option("-1","List one file per line")
 .option("-a","Include hidden file")
 .argument("[dir]", "Directory to list",".")
 .parse();

 const options = program.opts();
const dir = program.args[0] || ".";

try {
  const items = await fs.readdir(dir, { withFileTypes: true });

  let fileNames = items.map(item => item.name);

  // Filter out hidden files unless -a
  if (!options.a) {
    fileNames = fileNames.filter(name => !name.startsWith("."));
  }

  // Print output
  if (options["1"]) {
    // One file per line
    fileNames.forEach(name => console.log(name));
  } else {
    // Default: space-separated (like regular `ls`)
    console.log(fileNames.join("  "));
  }
} catch (err) {
  console.error(`Error reading directory "${dir}":`, err.message);
  process.exit(1);
}

