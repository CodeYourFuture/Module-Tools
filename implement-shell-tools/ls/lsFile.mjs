import process from "node:process";
import { promises as fs } from "node:fs";

const argv = process.argv.slice(2);

const dash = argv.filter(arg => arg.startsWith('-'));
const paths = argv.filter(arg => !arg.startsWith('-'));

const showAll = dash.includes('-a');

const targetDir = paths[0] ?? '.';

const entries = await fs.readdir(targetDir);

const result = showAll ? ['.', '..', ...entries] : entries.filter(e => !e.startsWith('.'));

for (const entry of result) {
    console.log(entry);
}
