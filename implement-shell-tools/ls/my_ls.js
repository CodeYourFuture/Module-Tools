import { readdirSync } from 'node:fs';
import { argv } from 'node:process';

const args = argv.slice(2); // skip node and script name

let showAll = false;
let dir = '.'; //set dir to current directory

// Parse args to check weather or not to show hidden files
//and ignore -1 because our output is already 1 per line
args.forEach(arg => {
  if (arg === '-a') {
    showAll = true;
  } else if (arg !== '-1') {
    dir = arg; //assumes anything else is our target directory
  }
});

try {
  let files = readdirSync(dir); // Reads the contents of the dir synchronously (readdirSync)

  if (!showAll) {
    files = files.filter(file => !file.startsWith('.'));
  }

  files.forEach(file => console.log(file));
} catch (err) {
  console.error(`Cannot access '${dir}': ${err.message}`);
}