import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

program
  .name("count-containing-lines-words-characters")
  .description("Counts lines, words or characters in a file (or all files) inside a directory")
  .option("-l, --line", "The number of lines in each file")
  .argument("<path>", "The file path to process");

program.parse();

const argv = program.args;