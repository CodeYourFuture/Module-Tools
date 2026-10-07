import {program} from 'commander';
import {promises as fs} from 'node:fs';
import process from 'node:process';

program
    .name('cat')
    .description('Concatenates and prints the contents of files.')
    .argument('<paths...>', 'The paths to the files to concatenate')
    .option('-n, --number', 'Number all output lines')
    .option('-b, --number-nonblank', 'Number nonempty output lines');

program.parse();

const argv = program.args;
const options = program.opts();

if (argv.length < 1) {
	console.error(
		`Expected at least 1 argument (a path) to be passed but got ${argv.length}.`,
	);
	process.exit(1);
}

let showLineNumbers = options.number || false;
let showNonEmptyLineNumbers = options.numberNonblank || false;

if (showLineNumbers && showNonEmptyLineNumbers) {
    showLineNumbers = false;
}

let lineNumber = 1;
const spacer = '    ';

for (const path of argv) {
    const content = await fs.readFile(path, 'utf-8');
    const lines = content.split('\n');
    while (lines.length > 0 && lines[lines.length - 1] === '') {
        lines.pop();
    }
    for (const line of lines) {
        if (showLineNumbers) {
            process.stdout.write(`${spacer} ${lineNumber++}  ${line}\n`);
        } else if (showNonEmptyLineNumbers && line.trim() !== '') {
            process.stdout.write(`${spacer} ${lineNumber++}  ${line}\n`);
        } else {
            process.stdout.write(`${line}\n`);
        }
    }
}