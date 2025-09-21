#!/usr/bin/env node
// wc.js — scaffold (no functionality yet)
// Plan:
//   1) single-file, no flags: print lines words bytes + filename
//   2) multiple files: print per-file + "total"
//   3) flags: -l (lines), -w (words), -c (bytes)

import { pathToFileURL } from "node:url";

function main() {
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.error("Usage: node wc.js <file...> | [-l|-w|-c] <file...>");
    process.exit(1);
  }
  console.log("wc: scaffold ready (implementation comes in next commit)");
}

// run only when executed directly
const isDirect = import.meta.url === pathToFileURL(process.argv[1]).href;
if (isDirect) main();
