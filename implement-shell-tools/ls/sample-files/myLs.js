#!/usr/bin/env node
const { program } = require("commander");
const fs = require("fs");
const path = require("path");

function listDirectory(dir, options) {
  let stats;
  try {
    stats = fs.statSync(dir);
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
  if (options.one) {
    names.forEach(name => console.log(name));
  } else {
    console.log(names.join("  "));
  }
}

program
  .name("myls")
  .description("Custom implementation of ls")
  .option("-1, --one", "list one file per line ")
  .option("-a, --all", "include hidden files and . and ..")
  .argument("[dir]", "directory to list", ".")
  .action((dir, options) => {
    listDirectory(dir, options);
  });

program.parse();
