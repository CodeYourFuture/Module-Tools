#!/usr/bin/env node
// wc.js — ESM: supports flags -l (lines), -w (words), -c (bytes)
// Behaviors covered by the README:
//   - wc sample-files/*
//   - wc -l sample-files/3.txt
//   - wc -w sample-files/3.txt
//   - wc -c sample-files/3.txt
//   - wc -l sample-files/*
// Also works with multiple flags (e.g., -lw), like GNU wc.

import fs from "node:fs";
import { pathToFileURL } from "node:url";

async function main() {
  const argv = process.argv.slice(2);

  let showLines = false;
  let showWords = false;
  let showBytes = false;
  const files = [];

  // Parse flags + files. Support combined short flags like -lw, -cl, etc.
  for (const arg of argv) {
    if (arg.startsWith("-") && arg !== "-") {
      for (const ch of arg.slice(1)) {
        if (ch === "l") showLines = true;
        else if (ch === "w") showWords = true;
        else if (ch === "c") showBytes = true;
        else {
          // ignore unknown short options for this assignment
        }
      }
    } else {
      files.push(arg);
    }
  }

  if (files.length === 0) {
    console.error("Usage: node wc.js [-l|-w|-c] <file...>");
    process.exit(1);
  }

  // No flags → show all three like wc
  const showAll = !showLines && !showWords && !showBytes;

  let hadError = false;
  let total = { lines: 0, words: 0, bytes: 0 };
  const results = [];

  for (const file of files) {
    try {
      const st = await fs.promises.lstat(file);
      if (st.isDirectory()) {
        console.error(`wc: ${file}: Is a directory`);
        hadError = true;
        continue;
      }
      const counts = await countFile(file);
      results.push({ file, ...counts });
      total.lines += counts.lines;
      total.words += counts.words;
      total.bytes += counts.bytes;
    } catch (err) {
      if (err?.code === "ENOENT") {
        console.error(`wc: ${file}: No such file or directory`);
      } else if (err?.code === "EACCES") {
        console.error(`wc: ${file}: Permission denied`);
      } else {
        console.error(`wc: ${file}: ${err?.message || "Error"}`);
      }
      hadError = true;
    }
  }

  for (const r of results) {
    console.log(formatRow(r, { showAll, showLines, showWords, showBytes }));
  }
  if (results.length > 1) {
    console.log(formatRow({ file: "total", ...total }, { showAll, showLines, showWords, showBytes }));
  }

  if (hadError) process.exitCode = 1;
}

async function countFile(file) {
  const buf = await fs.promises.readFile(file); // Buffer
  const bytes = buf.length;

  // Lines: count '\n' bytes
  let lines = 0;
  for (let i = 0; i < buf.length; i++) if (buf[i] === 0x0a) lines++;

  // Words: sequences of non-whitespace
  const text = buf.toString("utf8");
  const words = (text.match(/\S+/g) || []).length;

  return { lines, words, bytes };
}

function formatRow({ lines, words, bytes, file }, opts) {
  const cols = [];
  if (opts.showAll || opts.showLines) cols.push(pad(lines));
  if (opts.showAll || opts.showWords) cols.push(pad(words));
  if (opts.showAll || opts.showBytes) cols.push(pad(bytes));
  return `${cols.join(" ")} ${file}`;
}

function pad(n) {
  // Right-align like `wc`
  return String(n).padStart(7, " ");
}

// run only when executed directly
const isDirect = import.meta.url === pathToFileURL(process.argv[1]).href;
if (isDirect) await main();
