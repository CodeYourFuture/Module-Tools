#!/usr/bin/env node


import fs from "node:fs";
import { pathToFileURL } from "node:url";

const raw = process.argv.slice(2);

let includeAll = false;   // -a
let onePerLine = false;   // -1 (format already one-per-line)
const targets = [];

// Parse flags (supports combined like -a1 / -1a). Treat lone "-" as a path.
for (const arg of raw) {
  if (arg === "-" || !arg.startsWith("-")) {
    targets.push(arg);
    continue;
  }
  if (arg === "-1") {
    onePerLine = true;
    continue;
  }
  for (const ch of arg.slice(1)) {
    if (ch === "a") includeAll = true;
    else if (ch === "1") onePerLine = true;
    else {
      // ignore unknown short flags
    }
  }
}

const paths = targets.length ? targets : ["."];
let hadError = false;

for (let i = 0; i < paths.length; i++) {
  const p = paths[i];
  try {
    const st = await fs.promises.lstat(p);

    if (st.isDirectory()) {
      if (paths.length > 1) console.log(`${p}:`);

      const entries = await fs.promises.readdir(p, { withFileTypes: true });
      let names = entries.map(d => d.name);

      if (!includeAll) {
        names = names.filter(n => !n.startsWith("."));
      } else {
        // mimic `ls -a` by including "." and ".."
        names = ["." , "..", ...names];
      }

      names.sort((a, b) => a.localeCompare(b));
      for (const name of names) {
        // one-per-line output; -1 flag just affirms it
        console.log(name);
      }

      if (paths.length > 1 && i !== paths.length - 1) console.log("");
    } else {
      // file or symlink => print the argument as given
      console.log(p);
    }
  } catch (err) {
    if (err?.code === "ENOENT") {
      console.error(`ls: cannot access '${p}': No such file or directory`);
    } else if (err?.code === "EACCES") {
      console.error(`ls: cannot open directory '${p}': Permission denied`);
    } else {
      console.error(`ls: ${p}: ${err?.message || "Error"}`);
    }
    hadError = true;
  }
}

if (hadError) process.exitCode = 1;

// run only when executed directly
const isDirect = import.meta.url === pathToFileURL(process.argv[1]).href;
if (!isDirect) {
  // allow importing in tests without auto-executing
}
