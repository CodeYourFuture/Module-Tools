import process from "node:process";
import { promises as fs } from "node:fs";

const argv = process.argv.slice(2);

const dash = argv.filter(arg => arg.startsWith('-'));
const filePaths = argv.filter(arg => !arg.startsWith('-'));

const showLineNumbers = dash.includes('-n');
const showNonBlank = dash.includes('-b');

let lineCounter = 1;

for (const filePath of filePaths) {
    let content;
    try {
        content = await fs.readFile(filePath, 'utf8');
    } catch {
        console.error(`cat: ${filePath}: No file or directory exists`);
        process.exit(1);
    }

    const lines = content.split('\n');
    
    if (lines[lines.length - 1] === '') lines.pop();

    for (const line of lines) {
        const isBlank = line.trim() === '';

        if (showNonBlank) {
            if (isBlank) {
                console.log('');
            } else {
                console.log(`${String(lineCounter).padStart(6)}\t${line}`);
                lineCounter++;
            }
        } else if (showLineNumbers) {
            console.log(`${String(lineCounter).padStart(6)}\t${line}`);
            lineCounter++;
        } else {
            console.log(line);
        }
    }
}
