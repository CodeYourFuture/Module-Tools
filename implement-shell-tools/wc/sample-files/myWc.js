#!/usr/bin/env node
const { program } = require("commander");
const fs = require("fs");
const path = require("path");

function expandWildcard(pattern) {
  const dir = path.dirname(pattern);
  const base = path.basename(pattern);

  if (!base.includes("*")) return [pattern];

  let files;
  try {
    files = fs.readdirSync(dir);
  } catch {
    console.error(`wc: ${pattern}: No such directory`);
    return [];
  }

  const regex = new RegExp("^" + base.replace(/\*/g, ".*") + "$");
  return files
    .filter(f => regex.test(f))
    .map(f => path.join(dir, f));
}

function countLines(text) {
  if (text === "") return 0;
  const matches = text.match(/\n/g) || [];
  return text.endsWith("\n") ? matches.length : matches.length + 1;
}

function countWords(text) {
  return text.split(/\s+/).filter(Boolean).length;
}

function countChars(text) {
  return Buffer.byteLength(text, "utf-8");
}

function formatOutput({ lines, words, chars }, options, label) {
  const paddingSize = 7;

  const paddedLines = String(lines).padStart(paddingSize);
  const paddedWords = String(words).padStart(paddingSize);
  const paddedChars = String(chars).padStart(paddingSize);

  const onlyLines = options.lines && !options.words && !options.chars;
  const onlyWords = options.words && !options.lines && !options.chars;
  const onlyChars = options.chars && !options.lines && !options.words;

  if (onlyLines) return `${paddedLines} ${label}`;
  if (onlyWords) return `${paddedWords} ${label}`;
  if (onlyChars) return `${paddedChars} ${label}`;

  return `${paddedLines} ${paddedWords} ${paddedChars} ${label}`;
}

function wcFile(filename, options) {
  let text;
  try {
    text = fs.readFileSync(filename, "utf-8");
  } catch {
    console.error(`wc: ${filename}: No such file`);
    return null;
  }

  const counts = {
    lines: countLines(text),
    words: countWords(text),
    chars: countChars(text),
  };

  console.log(formatOutput(counts, options, filename));
  return counts;
}

program
  .name("mywc")
  .description("Custom implementation of wc")
  .option("-l, --lines", "count lines")
  .option("-w, --words", "count words")
  .option("-c, --chars", "count characters")
  .argument("<files...>", "files or wildcard patterns")
  .action((patterns, options) => {
    let allFiles = [];
    patterns.forEach(p => {
      allFiles = allFiles.concat(expandWildcard(p));
    });

    let totalLines = 0;
    let totalWords = 0;
    let totalChars = 0;

    allFiles.forEach(file => {
      const result = wcFile(file, options);
      if (result) {
        totalLines += result.lines;
        totalWords += result.words;
        totalChars += result.chars;
      }
    });

    if (allFiles.length > 1) {
      console.log(
        formatOutput(
          { lines: totalLines, words: totalWords, chars: totalChars },
          options,
          "total"
        )
      );
    }
  });

program.parse();
