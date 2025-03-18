//A simple script that reads a file and prints its content.(no flags yet)
const fs = require("fs");

const args = process.argv;
const files = args.slice(2); // No flags yet, just file names

console.log("args",args);
console.log("files",files);

function readCatFile(filePath) {
    try {
        const content = fs.readFileSync(filePath, "utf8");
        console.log(content);
    } catch (err){
        console.error(`error reading ${filePath}: ${err.message}`)
    }
}

files.forEach(file => readCatFile(file))
