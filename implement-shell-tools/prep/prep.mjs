import { program } from 'commander';
import process from 'node:process';
import { promises as fs } from 'node:fs';

program
    .name('prep')
    .description('Counts the number of words in a file that contain the letter "e".')
    .option('-c, --char <char>', 'The character to search for in words', 'e')
    .argument('<path>', 'The path to the file to analyze')

program.parse();    

const argv = program.args;

if (argv.length != 1) {
	console.error(
		`Expected exactly 1 argument (a path) to be passed but got ${argv.length}.`,
	);
	process.exit(1);
}
const path = argv[0];
const char = program.opts().char;

const content = await fs.readFile(path, 'utf-8');
const countOfWordsContainingChar = content
	.split(' ')
	.filter((word) => word.includes(char)).length;
console.log(countOfWordsContainingChar);
