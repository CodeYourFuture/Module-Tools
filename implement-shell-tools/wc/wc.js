const fs = require("fs");

const args = process.argv.slice(2);

const showLines = args.includes("-l");
const showWords = args.includes("-w");
const showBytes = args.includes("-c");

const files = args.filter(a => !a.startsWith("-"));

function getStats(text) {
  return {
    lines: text.split("\n").length - 1,
    words: text.trim().split(/\s+/).filter(Boolean).length,
    bytes: Buffer.byteLength(text)
  };
}

function format(num) {
  return String(num).padStart(8);
}

let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

files.forEach(file => {
  const content = fs.readFileSync(file, "utf8");
  const stats = getStats(content);

  totalLines += stats.lines;
  totalWords += stats.words;
  totalBytes += stats.bytes;

  let output = [];

  if (showLines) output.push(format(stats.lines));
  else if (showWords) output.push(format(stats.words));
  else if (showBytes) output.push(format(stats.bytes));
  else output.push(format(stats.lines), format(stats.words), format(stats.bytes));

  output.push(file);

  console.log(output.join(" "));
});

if (files.length > 1) {
  let output = [];

  if (showLines) output.push(format(totalLines));
  else if (showWords) output.push(format(totalWords));
  else if (showBytes) output.push(format(totalBytes));
  else output.push(format(totalLines), format(totalWords), format(totalBytes));

  output.push("total");

  console.log(output.join(" "));
}