#!/usr/bin/env node
// cat.js — scaffold (no functionality yet)
// Next commits will add:
//   - basic file output
//   - -n (number all lines)
//   - -b (number non-blank)

function main() {
  const args = process.argv.slice(2);
  if (args.length === 0) {
    console.error("Usage: node cat.js <file...>");
    process.exit(1);
  }
  console.log("cat: scaffold ready (implementation comes in next commit)");
}

if (require.main === module) main();
