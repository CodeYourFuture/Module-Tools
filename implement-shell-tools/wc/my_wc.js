import { promises as fs } from 'node:fs';
import { argv } from 'node:process';

const args = argv.slice(2);

if (args.length === 0) {
  console.error('Usage: node my_wc.mjs [-l] [-w] [-c] <file> [file2 ...]');
  process.exit(1);
}

// Parse flags and files
const flags = {
  l: false,
  w: false,
  c: false,
};

const files = [];

for (const arg of args) {
  if (arg.startsWith('-') && arg.length > 1) {
    for (const ch of arg.slice(1)) {
      if (flags.hasOwnProperty(ch)) {
        flags[ch] = true;
      } else {
        console.error(`Unknown option: -${ch}`);
        process.exit(1);
      }
    }
  } else {
    files.push(arg);
  }
}

if (files.length === 0) {
  console.error('Error: no files specified.');
  process.exit(1);
}

// If no flags specified, show all by default
const showLines = flags.l || (!flags.l && !flags.w && !flags.c);
const showWords = flags.w || (!flags.l && !flags.w && !flags.c);
const showBytes = flags.c || (!flags.l && !flags.w && !flags.c);

function pad(num, width = 8) {
  return num.toString().padStart(width, ' ');
}

function formatOutput({ lines, words, bytes }, label) {
  let output = '';
  if (showLines) output += pad(lines);
  if (showWords) output += pad(words);
  if (showBytes) output += pad(bytes);
  output += ` ${label}`;
  return output;
}

async function countFile(file) {
  try {
    const content = await fs.readFile(file, 'utf-8');
    const lines = content.split('\n').length - 1;
    const words = content.trim().split(/\s+/).filter(Boolean).length;
    const bytes = Buffer.byteLength(content, 'utf-8');

    const counts = { lines, words, bytes };
    console.log(formatOutput(counts, file));

    return counts;
  } catch (err) {
    console.error(`Cannot access '${file}': ${err.message}`);
    return null;
  }
}

async function main() {
  // Instead of .map, I can explicitly collect promises using forEach():
  const promises = [];
  files.forEach(file => {
    promises.push(countFile(file));
  });
  const counts = await Promise.all(promises);

  const validCounts = counts.filter(c => c !== null);

  if (validCounts.length > 1) {
    const totals = {
      lines: validCounts.reduce((sum, c) => sum + c.lines, 0),
      words: validCounts.reduce((sum, c) => sum + c.words, 0),
      bytes: validCounts.reduce((sum, c) => sum + c.bytes, 0),
    }

    console.log(formatOutput(totals, 'total'));
  }
}

main();
