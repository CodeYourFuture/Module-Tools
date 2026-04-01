const fs = require("fs");

// input from terminal
const args = process.argv.slice(2);

// check flags
const hasN = args.includes("-n");
const hasB = args.includes("-b");

// get only file names
const files = args.filter((arg) => !arg.startsWith("-"));

let count = 1;

// go through each file
for (let i = 0; i < files.length; i++) {
  const content = fs.readFileSync(files[i], "utf-8");

  const lines = content.split("\n");

  // go through each line
  for (let j = 0; j < lines.length; j++) {
    const line = lines[j];

    // if -b (number non-empty lines)
    if (hasB) {
      if (line.trim() !== "") {
        console.log(count + " " + line);
        count++;
      } else {
        console.log("");
      }
    }
    // if -n (number all lines)
    else if (hasN) {
      console.log(count + " " + line);
      count++;
    }
    // no flags
    else {
      console.log(line);
    }
  }
}
