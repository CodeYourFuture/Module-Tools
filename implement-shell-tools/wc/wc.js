import { program } from "commander";
import { promises as fs } from "node:fs";

program
    .name("wc")
    .description("word, line, and byte count")
    .option("-c", "Output the number of bytes")
    .option("-w", "Output the number of words")
    .option("-l", "Output the number of lines");

program.parse();

const opts = program.opts();
const showAll = !(opts.c || opts.w || opts.l);
const showBytes = opts.c || showAll;
const showWords = opts.w || showAll;
const showLines = opts.l || showAll;

function formatOutputLine(bytes, words, lines, path) {
    let line = "";
    if (showLines) {
        line += lines.toString().padStart(8);
    }
    if (showWords) {
        line += words.toString().padStart(8);
    }
    if (showBytes) {
        line += bytes.toString().padStart(8);
    }
    line += " " + path;
    return line;
}

let totalBytes = 0;
let totalWords = 0;
let totalLines = 0;
for (const path of program.args) {
    const content = await fs.readFile(path, "utf-8");
    const bytes = content.length;
    const words = content.split(/\s+/).filter((word) => word.length > 0).length;
    const rawLines = content.split("\n").length;
    const lines = (content.slice(-1) === "\n") ? rawLines - 1 : rawLines;
    totalBytes += bytes;
    totalWords += words;
    totalLines += lines;
    console.log(formatOutputLine(bytes, words, lines, path));
}
if (program.args.length > 1) {
    console.log(formatOutputLine(totalBytes, totalWords, totalLines, "total"));
}
