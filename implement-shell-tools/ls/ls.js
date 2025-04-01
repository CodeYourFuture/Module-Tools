const { promises: fs } = require("fs");
const { program } = require("commander");

program
  .name("ls")
  .description("An implementation of the ls command")
  .option("-a, --all", "Include hidden files")
  .option("-1", "List one file per line") // Support for -1 flag
  .argument("[directory]", "The directory to list", ".") // Default directory is "."
  .parse(process.argv);

const { all: showHidden, "1": onePerLine } = program.opts();
const directory = program.args[0] || "."; // Ensures a valid directory always used

async function listFiles(dir) {
  try {
    let files = await fs.readdir(dir); // Read directory contents

    if (!showHidden) {
      // Filter out hidden files if --all is not set
      files = files.filter(file => !file.startsWith("."));
    }

    if (onePerLine) {
      // Ensure one file per line
      files.forEach(file => console.log(file));
    } else {
      // Default behavior: print files space-separated (like ls without -1)
      console.log(files.join(" "));
    }
  } catch (err) {
    // Enhanced error handling to print ls behavior
    console.error(`ls: cannot access '${dir}': No such file or directory`);
  }
}

// Call the function with the specified directory
listFiles(directory);

