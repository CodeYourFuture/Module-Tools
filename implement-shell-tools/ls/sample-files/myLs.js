#!/usr/bin/env node
const { program } = require("commander");
const fs = require("fs");
const path = require("path");

function listDirectory(dir, options) {
  try {
    const stats = fs.statSync(dir);

    if (stats.isFile()) {
      console.log(dir);
      return; 
    }
  } catch (e) {
    console.error(`ls: cannot access '${dir}': No such file or directory`);
    return;
  }

  let entries;

  try {
    entries = fs.readdirSync(dir, { withFileTypes: true });
  } catch (e) {
    console.error(`ls: cannot access '${dir}': No such file or directory`);
    return;
  }

  let names = entries.map(e => e.name);

  if (options.all) {
    names.unshift(".", "..");
  } else {
    names = names.filter(name => !name.startsWith("."));
  }

  names.sort();
  names.forEach(name => console.log(name));
}

program
  .name("myls")
  .description("Custom implementation of ls")
  .option("-1", "list one file per line (default in our version)")
  .option("-a, --all", "include hidden files")
  .argument("[dir]", "directory to list", ".")
  .action((dir, options) => {
    listDirectory(dir, options);
  });

program.parse();