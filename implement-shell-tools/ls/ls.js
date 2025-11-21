import process from "node:process";
import { promises as fs } from "node:fs";
import { program } from "commander";

program
  .name("list-files-in-directory")
  .description("List all files and directories in a directory")
  .argument("<path>", "The file path to process")
  .option("-1", "Output one entry per line")
//   .option("-a", "List all files & directories, including hidden ones");

program.parse();

const path = program.args[0];

const options = program.opts();
