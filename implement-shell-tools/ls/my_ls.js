import { readdirSync } from 'node:fs';
import { argv } from 'node:process';

const args = argv.slice(2); // skips node and script name

const flags = args.filter(arg => arg.startsWith('-'));
const operands = args.filter(arg => !arg.startsWith('-'));

let showAll = flags.includes('-a');
let onePerLine = flags.includes('-1');

if (operands.length === 0) operands.push('.'); // defaults to current dir

operands.forEach(dir => {
  try {
    let files = readdirSync(dir);  // Reads the contents of the dir synchronously (readdirSync)

    if (!showAll) {
      files = files.filter(file => !file.startsWith('.'));
    }

    files.sort((a, b) => a.localeCompare(b));

    if (onePerLine) {
      files.forEach(file => console.log(file));
    } else {
      console.log(files.join('   '));
    }
  } catch (err) {
    console.error(`ls: cannot access '${dir}': ${err.message}`);
  }
});