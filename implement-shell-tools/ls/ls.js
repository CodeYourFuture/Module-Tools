const fs = require("fs");

const args = process.argv.slice(2);

let onePerLine = false;
let showHidden = false;
let paths = [];

for (let i = 0; i < args.length; i++) {
  if (args[i] === "-1") {
    onePerLine = true;
  } else if (args[i] === "-a") {
    showHidden = true;
  } else {
    paths.push(args[i]);
  }
}
if (paths.length === 0) {
  paths.push(".");
}

for (let i = 0; i < paths.length; i++) {
  let path = paths[i];

  try {
    if (fs.statSync(path).isFile()) {
      console.log(path);
    } else {
      let files = fs.readdirSync(path);

      files.sort();

      for (let j = 0; j < files.length; j++) {
        let file = files[j];
        if (!showHidden && file.startsWith(".")) {
          continue;
        }
        if (onePerLine) {
          console.log(file);
        } else {
          process.stdout.write(file + " ");
        }
      }

      if (!onePerLine) {
        process.stdout.write("\n");
      }
    }
  } catch (error) {
    console.log("Cannot access: " + path);
  }
}
