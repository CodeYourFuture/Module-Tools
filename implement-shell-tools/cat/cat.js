#!/usr/bin/env node
// cat.js — basic version (no flags)

import fs from 'fs';

const files = process.argv.slice(2);

if (files.length === 0) {
  console.error("Usage: node cat.js <file...>");
  process.exit(1);
}

let hadError = false;

(async () => {
  for (const file of files) {
    try {
      const stat = await fs.promises.stat(file);
      if (stat.isDirectory()) {
        console.error(`cat: ${file}: Is a directory`);
        hadError = true;
        continue;
      }
      await pipeFile(file);
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
})();

function pipeFile(file) {
  return new Promise((resolve, reject) => {
    const rs = fs.createReadStream(file);
    rs.on("error", reject);
    rs.on("end", resolve);
    // keep stdout open between files
    rs.pipe(process.stdout, { end: false });
  });
}
