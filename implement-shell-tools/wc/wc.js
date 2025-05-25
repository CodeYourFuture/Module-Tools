const { promises: fs } = require('fs');
const path = require('path');
const { program } = require('commander');

program
  .description('Count lines, words, and characters in the specified files')
  .option('-l, --lines', 'Count the lines')
  .option('-w, --words', 'Count the words')
  .option('-c, --characters', 'Count the characters')
  .parse(process.argv);

const options = program.opts();
const files = program.args;

if (files.length === 0) {
  console.error("Error: No files provided.");
  process.exit(1);
}

async function countFileStats(filePath, options) {
  try {
    const data = await fs.readFile(filePath, 'utf8');
    
    const lines = (data.match(/\n/g) || []).length;
    const words = data.split(/\s+/).filter(Boolean).length;
    const characters = data.length;
    
    const result = { lines, words, characters };
    const output = [];
    if (options.lines) output.push(result.lines);
    if (options.words) output.push(result.words);
    if (options.characters) output.push(result.characters);
    if (output.length === 0) output.push(result.lines, result.words, result.characters);
    
    return { file: filePath, output: output.join(' '), lines, words, characters };
  } catch (err) {
    console.error(`Error reading file: ${filePath}`);
    return null;
  }
}

async function processFiles() {
  let totalLines = 0;
  let totalWords = 0;
  let totalCharacters = 0;

  for (const file of files) {
    const filePath = path.resolve(file);
    const result = await countFileStats(filePath, options);

    if (result) {
      console.log(result.output, file);
      totalLines += result.lines;
      totalWords += result.words;
      totalCharacters += result.characters;
    }
  }

  if (files.length > 1) {
    const totals = [];
    if (options.lines) totals.push(totalLines);
    if (options.words) totals.push(totalWords);
    if (options.characters !== false) totals.push(totalCharacters);

    if (totals.length > 0) {
      console.log(totals.join(' ') + ' total');
    }
  }
}

processFiles();
