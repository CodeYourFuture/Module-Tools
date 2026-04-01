import process from "node:process";
import { promises as fs } from "node:fs";
import { Command } from "commander";

const program = new Command();

program
  .name("wc")
  .description("A simple node implementation of the word count utility")
  .argument("[files...]", "Files to process")
  .option("-l, --lines", "print the newline counts")
  .option("-w, --words", "print the word counts")
  .option("-c, --bytes", "print the byte counts")
  .action(async (files, options) => {
    // If no specific flags are provided, default to showing all
    const noFlagsProvided = !options.lines && !options.words && !options.bytes;
    const showAll = noFlagsProvided;

    const results = [];

    for (const filePath of files) {
      try {
        const stats = await calculateFileStats(filePath);
        results.push(stats);
        printReport(stats, options, showAll);
      } catch (error) {
        console.error(`wc: ${filePath}: No such file or directory`);
        process.exitCode = 1;
      }
    }

    if (results.length > 1) {
      const totals = {
        lineCount: results.reduce((sum, s) => sum + s.lineCount, 0),
        wordCount: results.reduce((sum, s) => sum + s.wordCount, 0),
        byteCount: results.reduce((sum, s) => sum + s.byteCount, 0),
        label: "total"
      };
      printReport(totals, options, showAll);
    }
  });

async function calculateFileStats(filePath) {
  const fileBuffer = await fs.readFile(filePath);
  const fileContent = fileBuffer.toString();

  return {
    lineCount: fileContent.split("\n").length - 1,
    wordCount: fileContent.split(/\s+/).filter(w => w.length > 0).length,
    byteCount: fileBuffer.length,
    label: filePath
  };
}

function printReport(stats, options, showAll) {
  const output = [];
  const format = (num) => String(num).padStart(4);

  if (showAll || options.lines) output.push(format(stats.lineCount));
  if (showAll || options.words) output.push(format(stats.wordCount));
  if (showAll || options.bytes) output.push(format(stats.byteCount));

  console.log(`${output.join("")} ${stats.label}`);
}

program.parse(process.argv);