const fs = require("fs");

const args = process.argv.slice(2);

const showAll = args.includes("-a");

const dirArg = args.find(arg => !arg.startsWith("-"));
const directory = dirArg || ".";

fs.readdir(directory, (err, files) => {
  if (err) {
    console.error(err.message);
    return;
  }

  let output = files;

  if (!showAll) {
    output = files.filter(file => !file.startsWith("."));
  } else {
    output = [".", "..", ...files];
  }

  output.forEach(file => console.log(file));
});