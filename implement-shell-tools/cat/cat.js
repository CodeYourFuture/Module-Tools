const fs = require("fs");

const args = process.argv.slice(2);

const numberAll = args[0] === "-n";
const numberNonBlank = args[0] === "-b";

const files = (numberAll || numberNonBlank)
    ? args.slice(1)
    : args;

let lineNumber = 1;

for (const file of files) {
    try {
        const content = fs.readFileSync(file, "utf8");
        const lines = content.endsWith("\n")
            ? content.slice(0, -1).split("\n")
            : content.split("\n");

        for (const line of lines) {
            if (numberAll) {
                console.log(`${String(lineNumber).padStart(6)}\t${line}`);
                lineNumber++;
            } else if (numberNonBlank && line !== "") {
                console.log(`${String(lineNumber).padStart(6)}\t${line}`);
                lineNumber++;
            } else {
                console.log(line);
            }
        }
    } catch (err) {
        console.error(`cat: ${file}: ${err.message}`);
    }
}