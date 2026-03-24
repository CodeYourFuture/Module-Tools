const fs = require("fs");

// Get command line arguments
const args = process.argv.slice(2);

// Default settings
let showAll = false;
let onePerLine = false;
let dir = ".";

// Parse arguments
args.forEach((arg) => {
  if (arg === "-a") {
    showAll = true;
  } else if (arg === "-1") {
    onePerLine = true;
  } else {
    dir = arg;
  }
});

// Read directory contents
let files = fs.readdirSync(dir);

// Filter hidden files if -a is NOT used
if (!showAll) {
  files = files.filter((file) => !file.startsWith("."));
}

// Output
if (onePerLine) {
  files.forEach((file) => console.log(file));
} else {
  console.log(files.join("  "));
}
