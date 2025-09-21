#!/usr/bin/env node
// ls.js — scaffold (no functionality yet)
// Next commits will add:
//   - basic listing of '.' or given paths (no flags)
//   - -a (include dotfiles)
//   - -1 (one entry per line; simple output format)
//   - -l (long format) [stretch if required]

import { pathToFileURL } from "node:url";

function main() {
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.error("Usage: node ls.js [path...]");
    process.exit(1);
  }
  console.log("ls: scaffold ready (implementation comes in next commit)");
}

// run only when executed directly
const isDirect = import.meta.url === pathToFileURL(process.argv[1]).href;
if (isDirect) main();
