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

function wcFile(filename, options) {
  let text;
  try {
    text = fs.readFileSync(filename, "utf-8");
  } catch {
    console.error(`wc: ${filename}: No such file`);
    return null;
  }

  const lineCount = countLines(text);
  const wordCount = countWords(text);
  const charCount = countChars(text);

  let output;
  const paddingSize = 7;
  if (options.lines && !options.words && !options.chars) output = `${lineCount} ${filename}`;
  else if (options.words && !options.lines && !options.chars) output = `${wordCount} ${filename}`;
  else if (options.chars && !options.lines && !options.words) output = `${charCount} ${filename}`;
  else output = `${String(lineCount).padStart(paddingSize)} ${String(wordCount).padStart(paddingSize)} ${String(charCount).padStart(paddingSize)} ${filename}`;
  console.log(output);

  return { lines: lineCount, words: wordCount, chars: charCount };
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
    patterns.forEach(p => allFiles = allFiles.concat(expandWildcard(p)));

    let totalLines = 0, totalWords = 0, totalChars = 0;

    allFiles.forEach(file => {
      const result = wcFile(file, options);
      if (result) {
        totalLines += result.lines;
        totalWords += result.words;
        totalChars += result.chars;
      }
    });
    const paddingSize = 7;
    if (allFiles.length > 1) {
      if (options.lines && !options.words && !options.chars) console.log(`${totalLines} total`);
      else if (options.words && !options.lines && !options.chars) console.log(`${totalWords} total`);
      else if (options.chars && !options.lines && !options.words) console.log(`${totalChars} total`);
      else console.log(
        `${String(totalLines).padStart(paddingSize)} ` +
        `${String(totalWords).padStart(paddingSize)} ` +
        `${String(totalChars).padStart(paddingSize)} total`);
    }
  });

program.parse();
