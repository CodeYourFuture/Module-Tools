#!/usr/bin/env node
// cat.js — ESM: supports -n and -b (-b overrides -n)

import fs from "node:fs";
import readline from "node:readline";

const args = process.argv.slice(2);
let numberAll = false;
let numberNonblank = false;
const files = [];

// parse flags + files (flags can appear anywhere)
for (const a of args) {
  if (a === "-n") numberAll = true;
  else if (a === "-b") numberNonblank = true;
  else files.push(a);
}
// precedence: -b wins over -n
if (numberNonblank) numberAll = false;

if (files.length === 0) {
  console.error("Usage: node cat.js [-n|-b] <file...>");
  process.exit(1);
}

let hadError = false;
let lineNo = 1;

for (const file of files) {
  try {
    const stat = await fs.promises.stat(file);
    if (stat.isDirectory()) {
      console.error(`cat: ${file}: Is a directory`);
      hadError = true;
      continue;
    }
    if (!numberAll && !numberNonblank) {
      await pipeFile(file);
    } else {
      await numberFile(file, { nonblank: numberNonblank });
    }
  } catch (err) {
    if (err?.code === "ENOENT" || err?.code === "ENOTDIR") {
      console.error(`cat: ${file}: No such file or directory`);
    } else {
      console.error(`cat: ${file}: ${err?.message || "Error"}`);
    }
    hadError = true;
  }
}

if (hadError) process.exitCode = 1;

function pipeFile(file) {
  return new Promise((resolve, reject) => {
    const rs = fs.createReadStream(file);
    rs.on("error", reject);
    rs.on("end", resolve);
    rs.pipe(process.stdout, { end: false }); // keep stdout open between files
  });
}

function numberFile(file, { nonblank }) {
  return new Promise((resolve, reject) => {
    const rs = fs.createReadStream(file);
    const rl = readline.createInterface({ input: rs, crlfDelay: Infinity });

    rl.on("line", (line) => {
      if (nonblank) {
        if (line.length === 0) {
          process.stdout.write("\n"); // blank line, no number
        } else {
          process.stdout.write(formatNum(lineNo++) + line + "\n");
        }
      } else {
        process.stdout.write(formatNum(lineNo++) + line + "\n");
      }
    });
    rl.on("close", resolve);
    rl.on("error", reject);
    rs.on("error", reject);
  });
}

function formatNum(n) {
  // GNU cat style: width 6, right-aligned, then a tab
  return String(n).padStart(6, " ") + "\t";
}
