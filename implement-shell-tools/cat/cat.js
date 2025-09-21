#!/usr/bin/env node
// cat.js — ESM version with -n (number all lines)

import fs from "node:fs";
import readline from "node:readline";

const args = process.argv.slice(2);
let numberAll = false;
const files = [];

// parse flags + files
for (const a of args) {
  if (a === "-n") numberAll = true;
  else files.push(a);
}

if (files.length === 0) {
  console.error("Usage: node cat.js [-n] <file...>");
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
    if (numberAll) {
      await numberFile(file);
    } else {
      await pipeFile(file);
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
    // keep stdout open between files
    rs.pipe(process.stdout, { end: false });
  });
}

function numberFile(file) {
  return new Promise((resolve, reject) => {
    const rs = fs.createReadStream(file);
    const rl = readline.createInterface({ input: rs, crlfDelay: Infinity });

    rl.on("line", (line) => {
      process.stdout.write(formatNum(lineNo++) + line + "\n");
    });
    rl.on("close", resolve);
    rl.on("error", reject);
    rs.on("error", reject);
  });
}

function formatNum(n) {
  // match GNU cat -n: 6-wide, right-aligned, then a tab
  return String(n).padStart(6, " ") + "\t";
}
