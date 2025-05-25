const fs = require('fs');
const { program } = require('commander');

program
  .option('-a, --all', 'Show hidden files')
  .option('-1', 'Show one file per line')
  .argument('[dirPaths...]', 'Directory paths', ['.']) // Support multiple directories
  .parse(process.argv);

const { all, '1': onePerLine } = program.opts();
const dirPaths = program.args;

function listDirectoryContents(dirPath, showHidden = false, onePerLine = false) {
  fs.readdir(dirPath, (err, files) => {
    if (err) {
      console.error(`Error reading directory '${dirPath}': ${err.message}`);
      return;
    }

    if (!showHidden) {
      files = files.filter(file => !file.startsWith('.'));
    }

    console.log(`\n${dirPath}:`);
    if (onePerLine) {
      files.forEach(file => console.log(file));
    } else {
      console.log(files.join(' '));
    }
  });
}

dirPaths.forEach(dirPath => {
  if (typeof dirPath !== 'string') {
    console.error(`Error: Invalid directory path '${dirPath}'`);
    return;
  }
  listDirectoryContents(dirPath, all, onePerLine);
});
