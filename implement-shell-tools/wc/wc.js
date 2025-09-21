#!/usr/bin/env node
// wc.js — ESM: single file, no flags
// Prints: lines words bytes  filename

import fs from "node:fs";
import { pathToFileURL } from "node:url";

async function main() {
  const args = process.argv.slice(2);

  // This commit supports exactly ONE file (no flags yet)
  if (args.length !== 1) {
    console.error("Usage (this commit): node wc.js <single-file>");
    process.exit(1);
  }

  const file = args[0];

  try {
    const buf = await fs.promises.readFile(file); // Buffer
    const bytes = buf.length;

    // Count lines: number of newline characters '\n'
    let lines = 0;
    for (let i = 0; i < buf.length; i++) {
      if (buf[i] === 0x0a) lines++; // '\n'
    }

    // Count words: sequences of non-whitespace
    const text = buf.toString("utf8");
    const words = (text.match(/\S+/g) || []).length;

    console.log(`${pad(lines)} ${pad(words)} ${pad(bytes)} ${file}`);
  } catch (err) {
    if (err?.code === "ENOENT") {
      console.error(`wc: ${file}: No such file or directory`);
    } else if (err?.code === "EACCES") {
      console.error(`wc: ${file}: Permission denied`);
    } else {
      console.error(`wc: ${file}: ${err?.message || "Error"}`);
    }
    process.exitCode = 1;
  }
}

function pad(n) {
  // Right-align like wc (fixed width helps match spacing)
  return String(n).padStart(7, " ");
}

// Run only when executed directly
const isDirect = import.meta.url === pathToFileURL(process.argv[1]).href;
if (isDirect) await main();
