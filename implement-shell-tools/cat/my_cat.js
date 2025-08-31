import { promises as fs } from 'node:fs';
import { argv } from 'node:process';

const args = argv.slice(2); // skip node and script name

let showLineNumb = false;
let showNoBlankNumb = false
const files = [];


args.forEach(arg => {
  if (arg === '-n') {
    showLineNumb = true;
  } else if (arg === '-b') {
    showNoBlankNumb = true;
  }else {  
    files.push(arg); 
  }
});

if (files.length === 0) {
  console.error('No input file specified');
  process.exit(1);
}

for (const file of files) {
  try {
    let content = await fs.readFile(file, 'utf-8');
    const lines = content.split('\n');

    if (showNoBlankNumb) {     // Number only non-blank lines
        let counter = 1;
        content = lines.map(line => 
          line.trim() === '' ? '' : `${counter++}\t${line}`
        ).join('\n');
    } else if (showLineNumb) {  // Number all lines
        content = lines.map((line, i) => `${i + 1}\t${line}`).join('\n');
    }
    console.log(content);
  } catch (err) {
  console.error(`Cannot access '${file}': ${err.message}`);
  }
}