import { promises as fs } from 'node:fs';
import { argv } from 'node:process';

const args = argv.slice(2); // skip node and script name

let showLineNumb = false;
let showNoBlankNumb = false
let file = '';


args.forEach(arg => {
  if (arg === '-n') {
    showLineNumb = true;
  } else if (arg === '-b') {
    showLineNumb = false;
    showNoBlankNumb = true;
  }else {  
    file = arg; 
  }
});

try {
  let content = await fs.readFile(file, 'utf-8');
  const lines = content.split('\n');

  if (showLineNumb) {
    // Number all lines
    content = lines.map((line, i) => `${i + 1}\t${line}`).join('\n');
  }else  if (showNoBlankNumb) {
    // Number only non-blank lines
    let counter = 1;
    content = lines.map(line => {
      if (line.trim() === '') return '';
      return `${counter++}\t${line}`;
    }).join('\n');
  }

  console.log (content)
} catch (err) {
  console.error(`Cannot access '${file}': ${err.message}`);
}