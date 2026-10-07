const fs = require("fs");

const args = process.argv.slice(2);

let oneLine = false;
let showHidden = false;
let targets = [];

for (const arg of args) {
    if (arg === "-1") {
        oneLine = true;
    } else if (arg === "-a") {
        showHidden = true;
    } else {
        targets.push(arg);
    }
}

if (targets.length === 0) {
    targets.push(".");
}

function listDirectory(directory) {
    let files = fs.readdirSync(directory);

    if (!showHidden) {
        files = files.filter(file => !file.startsWith("."));
    }

    files.sort();

    if (oneLine) {
        console.log(files.join("\n"));
    } else {
        console.log(files.join("  "));
    }
}

function listTarget(target) {
    try {
        const stats = fs.statSync(target);

        if (stats.isDirectory()) {
            listDirectory(target);
        } else {
            console.log(target);
        }

    } catch (error) {
        console.error(`ls: cannot access '${target}': No such file or directory`);
    }
}

for (const target of targets) {
    listTarget(target);
}