const fs = require("fs");

const args = process.argv.slice(2);

let flag = "";

for (const arg of args) {

    // Check for flags
    if (arg === "-n" || arg === "-b") {
        flag = arg;
        continue;
    }
    let lineNumber = 1;
    // Read the file
    const content = fs.readFileSync(arg, "utf8");

    // split into lines
    const lines = content.split("\n");

    // Remove the extra empty line if the file ends with a new line
    if (lines[lines.length - 1] === "") {
        lines.pop();
    }


    for (const line of lines) {

        if (flag === "-n") {
            console.log(`${String(lineNumber).padStart(6)}\t${line}`);
            lineNumber++;
        } else if (flag === "-b") {
            if (line === "") {
                console.log("");
            } else {
                console.log(`${String(lineNumber).padStart(6)}\t${line}`);
                lineNumber++;
            }
        } else {
            console.log(line);
        }
    }
}