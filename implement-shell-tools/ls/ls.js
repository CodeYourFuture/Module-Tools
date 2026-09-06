const fs = require("fs");
const path = require("path");
const args = process.argv.slice(2);

let onePerLine = false;
let showAll = false;
let target = ".";

for (const arg of args) {

    if (arg === "-1") {
        onePerLine = true;
    }
    else if (arg === "-a") {
        showAll = true;
    }
    else {
        target = arg;
    }
}

const stats = fs.statSync(target);
if (stats.isFile()) {
    console.log(target);
} else {

    let files = fs.readdirSync(target);

if (showAll) {
    files = [".", "..", ...files];
} else {
    files = files.filter(file => !file.startsWith("."));
}

if (onePerLine) {
    for (const file of files) {
        console.log(file);
    }
} else {
    console.log(files.join("   "));
}
}