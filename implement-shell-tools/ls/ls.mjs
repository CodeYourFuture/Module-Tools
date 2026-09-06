import { program } from 'commander';
import process from 'node:process';
import { promises as fs } from 'node:fs';

program
    .name('ls')
    .description('Lists the contents of a directory.')
    .argument('[path]', 'The path to the directory to list, defaults to the current directory')
    .option('-a, --all', 'Do not ignore entries starting with .')
    .option('-1', 'List one file per line');

program.parse();

const argv = program.args;
const path = argv[0] || '.';

let showAll = program.opts().all || false;
let onePerLine = program.opts()['1'] || false;

try {
    const files = await fs.readdir(path);
    files.sort((a, b) => a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' }));
    for (const file of files) {
        if (showAll || !file.startsWith('.')) {
            if (onePerLine) {
                process.stdout.write(`${file}\n`);
            } else {
                process.stdout.write(`${file} `);
            }
        }
    }
} catch (err) {
    process.stderr.write(`cannot access '${path}': No such file or directory\n`);
    process.exit(1);
}
