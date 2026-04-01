import process from "node:process";
import { promises as fs } from "node:fs";

/**
 * Calculates the lines, words, and bytes for a given file.
 */
async function calculateFileStats(filePath) {
  const fileBuffer = await fs.readFile(filePath);
  const fileContent = fileBuffer.toString();

  // Standard 'wc' counts newline characters (\n)
  const lineCount = fileContent.split("\n").length - 1;

  // Split by any whitespace and filter out empty strings to get actual words
  const wordCount = fileContent
    .split(/\s+/)
    .filter((word) => word.length > 0).length;

  // Buffer.length provides the exact byte count on disk
  const byteCount = fileBuffer.length;

  return { lineCount, wordCount, byteCount, filePath };
}

/**
 * Main execution function
 */
async function runWordCount() {
  const filePaths = process.argv.slice(2);
  const results = [];

  for (const filePath of filePaths) {
    try {
      const stats = await calculateFileStats(filePath);
      results.push(stats);

      printFormattedLine(
        stats.lineCount,
        stats.wordCount,
        stats.byteCount,
        stats.filePath,
      );
    } catch (error) {
      console.error(`wc: ${filePath}: No such file or directory`);
      process.exitCode = 1;
    }
  }

  // If multiple files were processed, show the total
  if (results.length > 1) {
    const totalLines = results.reduce((sum, item) => sum + item.lineCount, 0);
    const totalWords = results.reduce((sum, item) => sum + item.wordCount, 0);
    const totalBytes = results.reduce((sum, item) => sum + item.byteCount, 0);

    printFormattedLine(totalLines, totalWords, totalBytes, "total");
  }
}

/**
 * Formats the output into columns to match the standard 'wc' utility
 */
function printFormattedLine(lines, words, bytes, label) {
  const format = (number) => String(number).padStart(8);
  console.log(`${format(lines)}${format(words)}${format(bytes)} ${label}`);
}

runWordCount();
