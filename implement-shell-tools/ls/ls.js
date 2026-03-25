import process from 'node:process';
import fs from 'node:fs';

const argv = process.argv.slice(2)

const folderPath = argv[0] || ".";

const contents = fs.readdirSync(folderPath);

console.log(contents.join("  "));