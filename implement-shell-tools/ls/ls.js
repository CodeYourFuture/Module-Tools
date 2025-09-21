#!/usr/bin/env node
// ls.js — ESM basic version (no flags)
// - If no paths: list '.'
// - Excludes dotfiles by default
// - One entry per line, alphabetical
// - Multiple paths: print "path:" header before each directory group
// - GNU-like errors; exit code 1 on any failure

import fs from "node:fs";
import { pathToFileURL } from "node:url";

const args = process.argv.slice(2);
const targets = args.length ? args : ["."];
let hadError = false;

for (let i = 0; i < targets.length; i++) {
  const target = targets[i];

  try {
    const stat = await fs.promises.lstat(target);

    if (stat.isDirectory()) {
      if (targets.length > 1) console.log(`${target}:`);

      const entries = await fs.promises.readdir(target, { withFileTypes: true });
      const names = entries
        .map(d => d.name)
        .filter(n => !n.startsWith("."))               // no dotfiles (we’ll add -a later)
        .sort((a, b) => a.localeCompare(b));

      for (const name of names) console.log(name);

      if (targets.length > 1 && i !== targets.length - 1) console.log(""); // blank line between dir groups
    } else {
      // plain file or symlink -> print the argument as given
      console.log(target);
    }
  } catch (err) {
    if (err?.code === "ENOENT") {
      console.error(`ls: cannot access '${target}': No such file or directory`);
    } else if (err?.code === "EACCES") {
      console.error(`ls: cannot open directory '${target}': Permission denied`);
    } else {
      console.error(`ls: ${target}: ${err?.message || "Error"}`);
    }
    hadError = true;
  }
}

if (hadError) process.exitCode = 1;

// run only when executed directly
const isDirect = import.meta.url === pathToFileURL(process.argv[1]).href;
if (!isDirect) {
  // allow import in tests without auto-running
}
