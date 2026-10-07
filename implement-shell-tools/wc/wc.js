const fs = require("fs");

const args = process.argv.slice(2);

let showWords = false;
let showChars = false;
let showLines = false;
let fileNames = [];

// Check flags and file names
for (const item of args) {
    if (item === "-l") {
        showLines = true;
    } else if (item === "-w") {
        showWords = true;
    } else if (item === "-c") {
        showChars = true;
    } else {
        fileNames.push(item);
    }
}

// If no flags are given, show everything
if (!showLines && !showWords && !showChars) {
    showLines = true;
    showWords = true;
    showChars = true;
}

let grandLines = 0;
let grandWords = 0;
let grandChars = 0;

for (const fileName of fileNames) {
    const text = fs.readFileSync(fileName, "utf8");

    const totalLines = text.split("\n").length - 1;

    const trimmed = text.trim();
    const totalWords = trimmed ? trimmed.split(/\s+/).length : 0;

    const totalChars = Buffer.byteLength(text);

    grandLines += totalLines;
    grandWords += totalWords;
    grandChars += totalChars;

    let output = "";

    if (showLines) output += String(totalLines).padStart(8);
    if (showWords) output += String(totalWords).padStart(8);
    if (showChars) output += String(totalChars).padStart(8);

    output += " " + fileName;

    console.log(output);
}

if (fileNames.length > 1) {
    let output = "";

    if (showLines) output += String(grandLines).padStart(8);
    if (showWords) output += String(grandWords).padStart(8);
    if (showChars) output += String(grandChars).padStart(8);

    output += " total";

    console.log(output);
}