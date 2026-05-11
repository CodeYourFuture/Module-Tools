import { program } from "commander";
import { promises as fs } from "node:fs";

program.name("wc");
program.description("simple wc clone");
program.option("-w, --words", "print word count");
program.option("-l, --lines", "print line count");
program.option("-c, --bytes", "print byte count");
program.argument("[paths...]", "file(s) to process");
program.parse();

const options = program.opts();
const paths = program.args;

const noFlags = !options.words && !options.lines && !options.bytes;
const showWords = options.words || noFlags;
const showLines = options.lines || noFlags;
const showBytes = options.bytes || noFlags;

function count(content) {
  const lines = content.split("\n").length - 1;
  const words = content.trim().split(/\s+/).filter(Boolean).length;
  const bytes = Buffer.byteLength(content);

  return { lines, words, bytes };
}

function formatCounts({ lines, words, bytes }, label = "") {
  const output = [];

  if (showLines) {
    output.push(lines.toString().padStart(8));
  }

  if (showWords) {
    output.push(words.toString().padStart(8));
  }

  if (showBytes) {
    output.push(bytes.toString().padStart(8));
  }

  if (label) {
    output.push(label);
  }

  return output.join(" ");
}

async function processFile(path) {
  try {
    const stat = await fs.stat(path);

    if (stat.isDirectory()) {
      console.error(`${path}: Is a directory`);
      return;
    }

    const content = await fs.readFile(path, { encoding: "utf-8" });
    const counts = count(content);
    const output = formatCounts(counts, path);

    console.log(output);
  } catch (err) {
    console.error(`${path}: ${err.message}`);
  }
}

try {
  for (const path of paths) {
    await processFile(path);
  }
} catch (err) {
  console.error(err.message);
}
