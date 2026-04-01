#!/usr/bin/env node

import process from "node:process";
import { program } from "commander";
import { promises as fs } from "node:fs";

program
  .name("cls")
  .description("List contents of a directory")
  .option("-1", "Force output to be one entry per line")
  .option("-a", "Include hidden files")
  .argument("[path...]", "directories to list");

program.parse();

const options = program.opts();
const targetPaths = program.args.length > 0 ? program.args : ["."];

async function listDir(dirPath, showHeader) {
  try {
    let contents = await fs.readdir(dirPath);

    if (options.a) {
      contents.push(".", "..");
    } else {
      contents = contents.filter((name) => !name.startsWith("."));
    }

    contents.sort();

    if (showHeader) {
      process.stdout.write(`${dirPath}:\n`);
    }

    if (options["1"]) {
      contents.forEach((item) => process.stdout.write(`${item}\n`));
    } else {
      process.stdout.write(`${contents.join("   ")}\n`);
    }
  } catch (error) {
    console.error(`cls: ${dirPath}: ${error.message}`);
    process.exit(1);
  }
}

for (let i = 0; i < targetPaths.length; i++) {
  const path = targetPaths[i];
  const isMultiplePath = targetPaths.length > 1;

  await listDir(path, isMultiplePath);

  if (isMultiplePath && i < targetPaths.length - 1) process.stdout.write(`\n`);
}
