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

async function countFile(file) {
  try {
    const content = await fs.readFile(file, 'utf-8');
    const lines = content.split('\n').filter(line => line.trim() !== '').length;
    const words = content.trim().split(/\s+/).filter(Boolean).length;
    const bytes = Buffer.byteLength(content, 'utf-8');

    let output = '';
    if (showLines) output += `${lines} `;
    if (showWords) output += `${words} `;
    if (showBytes) output += `${bytes} `;

    output += file;

    console.log(output.trim());

    return { lines, words, bytes };
  } catch (err) {
    console.error(`Cannot access '${file}': ${err.message}`);
    return null;
  }
}

async function main() {
  const counts = await Promise.all(files.map(countFile));

  const validCounts = counts.filter(c => c !== null);

  if (validCounts.length > 1) {
    const totalLines = validCounts.reduce((sum, c) => sum + c.lines, 0);
    const totalWords = validCounts.reduce((sum, c) => sum + c.words, 0);
    const totalBytes = validCounts.reduce((sum, c) => sum + c.bytes, 0);

    let totalOutput = '';
    if (showLines) totalOutput += `${totalLines} `;
    if (showWords) totalOutput += `${totalWords} `;
    if (showBytes) totalOutput += `${totalBytes} `;

    totalOutput += 'total';

    console.log(totalOutput.trim());
  }
}

main();
