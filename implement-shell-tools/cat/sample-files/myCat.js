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
    console.error(`cat: ${pattern}: No such directory`);
    return [];
  }

  const regex = new RegExp("^" + base.replace(/\*/g, ".*") + "$");

  return files
    .filter((f) => regex.test(f))
    .map((f) => path.join(dir, f));
}

function printFile(filename, options) {
  let text;
  try {
    text = fs.readFileSync(filename, "utf-8");
  } catch {
    console.error(`cat: ${filename}: No such file`);
    return;
  }

  const lines = text.split("\n");
  if (lines[lines.length - 1] === "") lines.pop();

  let counter = 1;
  const paddingSize = 6;

  lines.forEach((line) => {
    const isEmpty = line.trim() === "";

    const shouldNumber =
      options.numberAll ||
      (options.numberNonempty && !isEmpty);

    if (shouldNumber) {
      console.log(
        `${String(counter).padStart(paddingSize)}  ${line}`
      );
      counter++;
    } else {
      console.log(line);
    }
  });
}

program
  .name("mycat")
  .description("A custom implementation of the cat command")
  .argument("<files...>", "files or wildcard patterns")
  .option("-n, --number-all", "number all lines")
  .option("-b, --number-nonempty", "number non-empty lines")
  .action((patterns, options) => {
    let allFiles = [];

    patterns.forEach((p) => {
      allFiles = allFiles.concat(expandWildcard(p));
    });

    allFiles.forEach((file) => printFile(file, options));
  });

program.parse();
