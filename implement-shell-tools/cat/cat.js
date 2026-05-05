const fs = require("fs");

const args = process.argv.slice(2);

const showN = args.includes("-n");
const showB = args.includes("-b");

const files = args.filter(a => !a.startsWith("-"));

let content = files.map(f => fs.readFileSync(f, "utf8")).join("");

let lines = content.split("\n");

// remove ONLY final empty line caused by trailing newline
if (lines[lines.length - 1] === "") {
  lines.pop();
}

let output = [];

if (showN) {
  let i = 1;
  for (const line of lines) {
    output.push(`${String(i).padStart(6)}  ${line}`);
    i++;
  }
} else if (showB) {
  let i = 1;
  for (const line of lines) {
    if (line !== "") {
      output.push(`${String(i).padStart(6)}  ${line}`);
      i++;
    } else {
      output.push("");
    }
  }
} else {
  output = lines;
}

// IMPORTANT: add final newline like real cat
process.stdout.write(output.join("\n") + "\n");