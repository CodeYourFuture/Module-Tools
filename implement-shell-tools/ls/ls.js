const fs = require('fs');
const { program } = require('commander');

program
  .option('-a, --all', 'Show hidden files')
  .option('-1', 'Show one file per line')
  .argument('[dirPath]', 'Directory path', '.')
  .parse(process.argv);

const { all, '1': onePerLine } = program.opts();
const dirPath = program.args[0] || '.'; 

if (typeof dirPath !== 'string') {
  console.error('Error: Invalid directory path');
  process.exit(1);
}

function listDirectoryContents(dirPath, showHidden = false, onePerLine = false) {
  fs.readdir(dirPath, (err, files) => {
    if (err) {
      console.error(`Error reading directory: ${err.message}`);
      return;
    }

    if (!showHidden) {
      files = files.filter(file => !file.startsWith('.'));
    }

    if (onePerLine) {
      files.forEach(file => console.log(file)); 
    } else {
      console.log(files.join(' ')); 
    }
  });
}

listDirectoryContents(dirPath, all, onePerLine);
