import fs from 'node:fs';

const folderPath = '.';

const contents = fs.readdirSync(folderPath);

console.log(contents.join("  "));