const fs = require("fs");

const args = process.argv.slice(2);

let flags = [];
let paths = [];

// Check arguments: separate flags and paths
args.forEach((arg) => {
  if (arg.startsWith("-")) {
    flags.push(arg);
  } else {
    paths.push(arg);
  }
});

// If no path is provided, use the current directory
if (paths.length === 0) {
  paths = ["."];
}

paths.forEach((path) => {
  if (fs.statSync(path).isFile()) {
    console.log(path);
  } else {
    let contents = fs.readdirSync(path);

    // Hide hidden files unless -a exists
    if (!flags.includes("-a")) {
      contents = contents.filter((file) => !file.startsWith("."));
    }

    // Check -1 flag
    if (flags.includes("-1")) {
      console.log(contents.join("\n"));
    } else {
      console.log(contents.join(" "));
    }
  }
});
