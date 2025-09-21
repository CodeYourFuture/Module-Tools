#!/usr/bin/env node
// wc.js — ESM: multiple files + total (no flags)
// Prints per-file: lines words bytes  filename
// If given >1 files, also prints a "total" line.

import fs from "node:fs";
import { pathToFileURL } from "node:url";

async function main() {
  const files = process.argv.slice(2);
  if (files.length === 0) {
    console.error("Usage (this commit): node wc.js <file...>");
    process.exit(1);
  }

  let hadError = false;
  let totalLines = 0, totalWords = 0, totalBytes = 0;
  const results = [];

  for (const file of files) {
    try {
      const st = await fs.promises.lstat(file);
      if (st.isDirectory()) {
        console.error(`wc: ${file}: Is a directory`);
        hadError = true;
        continue;
      }
      const { lines, words, bytes } = await countFile(file);
      results.push({ file, lines, words, bytes });
      totalLines += lines; totalWords += words; totalBytes += bytes;
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
    console.log(`${pad(r.lines)} ${pad(r.words)} ${pad(r.bytes)} ${r.file}`);
  }
  if (results.length > 1) {
    console.log(`${pad(totalLines)} ${pad(totalWords)} ${pad(totalBytes)} total`);
  }

  if (hadError) process.exitCode = 1;
}

async function countFile(file) {
  const buf = await fs.promises.readFile(file); // Buffer
  const bytes = buf.length;

  // lines: count '\n' bytes
  let lines = 0;
  for (let i = 0; i < buf.length; i++) if (buf[i] === 0x0a) lines++;

  // words: sequences of non-whitespace (on UTF-8 text)
  const text = buf.toString("utf8");
  const words = (text.match(/\S+/g) || []).length;

  return { lines, words, bytes };
}

function pad(n) {
  // Right-align like `wc` (fixed width works well for visual parity)
  return String(n).padStart(7, " ");
}

// run only when executed directly
const isDirect = import.meta.url === pathToFileURL(process.argv[1]).href;
if (isDirect) await main();
