const fs = require("fs");
const path = require("path");

// arguments
const args = process.argv.slice(2);

let isNumbered = false;
let isNumberNonEmpty = false;
const filePaths = [];

// parse args
args.forEach((arg) => {
  if (arg === "-n") {
    isNumbered = true;
  } else if (arg === "-b") {
    isNumberNonEmpty = true;
  } else {
    filePaths.push(arg);
  }
});

// -b overrides -n
if (isNumberNonEmpty) {
  isNumbered = false;
}

let lineNumber = 1;

// process files
filePaths.forEach((filePath, fileIndex) => {
  const content = fs.readFileSync(filePath, "utf-8");

  // split lines but keep empty ones
  const lines = content.split("\n");

  lines.forEach((line, index) => {
    const isLastLineOfLastFile =
      fileIndex === filePaths.length - 1 && index === lines.length - 1;

    if (isNumberNonEmpty) {
      if (line !== "") {
        console.log(`${lineNumber} ${line}`);
        lineNumber++;
      } else {
        console.log(line);
      }
    } else if (isNumbered) {
      console.log(`${lineNumber} ${line}`);
      lineNumber++;
    } else {
      console.log(line);
    }
  });
});
