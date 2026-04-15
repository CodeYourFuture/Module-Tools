#!/usr/bin/env node

const fs = require('fs');

function cat(files, options) {
  let lineNumber = 1;

  files.forEach((file) => {
    try {
      const data = fs.readFileSync(file, 'utf8');
      const lines = data.split('\n');
      const hasTrailingNewline = data.endsWith('\n');

      lines.forEach((line, index) => {
        const isVirtualTrailingLine = hasTrailingNewline && index === lines.length - 1;
        if (isVirtualTrailingLine) {
          return;
        }

        let prefix = '';
        const shouldNumberLine = options.numberLines || (options.numberNonEmpty && line.length > 0);
        if (shouldNumberLine) {
          prefix = `${String(lineNumber).padStart(6)}\t`;
          lineNumber++;
        }

        const shouldAppendNewline = hasTrailingNewline || index < lines.length - 1;
        process.stdout.write(`${prefix}${line}${shouldAppendNewline ? '\n' : ''}`);
      });
    } catch (err) {
      if (err.code === 'ENOENT') {
        console.error(`cat: ${file}: No such file or directory`);
      } else if (err.code === 'EACCES') {
        console.error(`cat: ${file}: Permission denied`);
      } else {
        console.error(`cat: ${file}: An error occurred`);
      }
      process.exit(1);
    }
  });
}

function main() {
  const args = process.argv.slice(2);
  const options = {
    numberLines: false,
    numberNonEmpty: false,
  };

  const files = [];

  args.forEach((arg) => {
    if (arg === '-n') {
      options.numberLines = true;
    } else if (arg === '-b') {
      options.numberNonEmpty = true;
    } else {
      files.push(arg);
    }
  });

  if (files.length === 0) {
    console.error('Usage: node cat.js [-n | -b] <file>...');
    process.exit(1);
  }

  cat(files, options);
}

main();