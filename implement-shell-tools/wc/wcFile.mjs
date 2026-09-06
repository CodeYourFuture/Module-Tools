import process from "node:process";
import { promises as fs } from "node:fs";

const argv = process.argv.slice(2);

const dash = argv.filter(arg => arg.startsWith('-'));
const filePaths = argv.filter(arg => !arg.startsWith('-'));

const forLines = dash.includes('-l');
const forWords = dash.includes('-w');
const forBytes = dash.includes('-c');

let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

for (const filePath of filePaths) {
    let content;
    try {
        content = await fs.readFile(filePath, 'utf8');
    } catch {
        console.error(`wc: ${filePath}: No file or directory exists`);
        process.exit(1);
    }

    const lines = content.split('\n').length - 1;
    const words = content.trim() === '' ? 0 : content.trim().split(/\s+/).length;
    const bytes = Buffer.byteLength(content, 'utf8');

    totalLines += lines;
    totalWords += words;
    totalBytes += bytes;

    if (forLines) {
        console.log(`${String(lines).padStart(8)} ${filePath}`);
    } else if (forWords) {
        console.log(`${String(words).padStart(8)} ${filePath}`);
    } else if (forBytes) {
        console.log(`${String(bytes).padStart(8)} ${filePath}`);
    } else {
        console.log(`${String(lines).padStart(8)} ${String(words).padStart(8)} ${String(bytes).padStart(8)} ${filePath}`);
    }
}

if (filePaths.length > 1) {
    if (forLines) {
        console.log(`${String(totalLines).padStart(8)} total`);
    } else if (forWords) {
        console.log(`${String(totalWords).padStart(8)} total`);
    } else if (forBytes) {
        console.log(`${String(totalBytes).padStart(8)} total`);
    } else {
        console.log(`${String(totalLines).padStart(8)} ${String(totalWords).padStart(8)} ${String(totalBytes).padStart(8)} total`);
    }
}
