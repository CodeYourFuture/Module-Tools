import { program } from 'commander';
import process from 'node:process';
import { promises as fs } from 'node:fs';

program
    .name('wc')
    .description('Counts the number of lines, words, and characters in a file.')
    .argument('<path>', 'The path to the file to analyze')

program.parse();

const argv = program.args;

if (argv.length != 1) {
    console.error(
        `Expected exactly 1 argument (a path) to be passed but got ${argv.length}.`);
    process.exit(1);
}
const path = argv[0];

const content = await fs.readFile(path, 'utf-8');
const lineCount = content.split('\n').filter(Boolean).length;
const wordCount = content.split(' ').filter(Boolean).length;
const characterCount = content.length;
console.log(` ${lineCount}  ${wordCount} ${characterCount} ${path}`);