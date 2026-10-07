const fs = require("fs");

const args = process.argv.slice(2);

let flag = "";
let filePaths = [];

if (args[0] && args[0].startsWith("-")) {
  flag = args[0];
  filePaths = args.slice(1);
} else {
  filePaths = args;
}

// Read all files into one string
let content = filePaths.map((file) => fs.readFileSync(file, "utf-8")).join("");

// Split into lines
let lines = content.split(/\r?\n/);

// Remove the last empty line if the file ends with a newline
if (lines[lines.length - 1] === "") {
  lines.pop();
}

// Handle flag ==> -n adding number to the line;
if (flag === "-n") {
  lines = lines.map((line, index) => {
    return `${index + 1}  ${line}`;
  });
}

// Handle flag ==> -b avoids adding number to empty line
if (flag === "-b") {
  let lineNumber = 1;

  lines = lines.map((line) => {
    if (line.trim() === "") {
      return line;
    }

    return `${lineNumber++}  ${line}`;
  });
}

process.stdout.write(lines.join("\n"));

