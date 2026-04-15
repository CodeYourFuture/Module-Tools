#!/usr/bin/env node

const fs = require('fs');

function countFile(file) {
  try {
    const data = fs.readFileSync(file, 'utf8');

    const lines = (data.match(/\n/g) || []).length;
    const words = data.split(/\s+/).filter(Boolean).length;
    const bytes = Buffer.byteLength(data, 'utf8');

    return { lines, words, bytes };
  } catch (err) {
    console.error(`wc: ${file}: ${err.code === 'ENOENT' ? 'No such file or directory' : 'An error occurred'}`);
    process.exit(1);
  }
}

function selectedKeys(options) {
  const keys = [];
  if (options.lines) keys.push('lines');
  if (options.words) keys.push('words');
  if (options.bytes) keys.push('bytes');
  return keys;
}

function valuesForKeys(counts, keys) {
  return keys.map((key) => counts[key]);
}

function printRows(rows, keys) {
  const alignColumns = keys.length > 1 || rows.length > 1;

  if (!alignColumns) {
    const [values, name] = rows[0];
    console.log(`${values[0]} ${name}`);
    return;
  }

  const widths = keys.map((_, index) => {
    const maxLen = Math.max(...rows.map(([values]) => String(values[index]).length));
    return Math.max(3, maxLen);
  });

  rows.forEach(([values, name]) => {
    const formattedValues = values
      .map((value, index) => String(value).padStart(widths[index], ' '))
      .join(' ');
    console.log(`${formattedValues} ${name}`);
  });
}

function main() {
  const args = process.argv.slice(2);
  const options = {
    lines: false,
    words: false,
    bytes: false,
  };

  const files = [];

  args.forEach((arg) => {
    if (arg === '-l') {
      options.lines = true;
    } else if (arg === '-w') {
      options.words = true;
    } else if (arg === '-c') {
      options.bytes = true;
    } else {
      files.push(arg);
    }
  });

  if (!options.lines && !options.words && !options.bytes) {
    options.lines = true;
    options.words = true;
    options.bytes = true;
  }

  if (files.length === 0) {
    console.error('Usage: wc [-l | -w | -c] <file>...');
    process.exit(1);
  }

  let totalLines = 0;
  let totalWords = 0;
  let totalBytes = 0;
  const keys = selectedKeys(options);
  const rows = [];

  files.forEach((file) => {
    const counts = countFile(file);
    const { lines, words, bytes } = counts;
    totalLines += lines;
    totalWords += words;
    totalBytes += bytes;
    rows.push([valuesForKeys(counts, keys), file]);
  });

  if (files.length > 1) {
    rows.push([valuesForKeys({ lines: totalLines, words: totalWords, bytes: totalBytes }, keys), 'total']);
  }

  printRows(rows, keys);
}

main();