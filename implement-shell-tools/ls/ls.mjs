import {program} from "commander";
import {promises as fs} from "node:fs";

program
  .name("ls")
  .description("List all the files in a directory")
  .option("-a, --all", "Include hidden files")
  .option("-1, --one", "One entry per line")
  .argument("[dir]", "directory to list");

program.parse();

const options = program.opts();
const dir = program.args[0] || ".";

let entries;
try {
    entries = await fs.readdir(dir, { withFileTypes: true });
} catch (err) {
    console.error(`Error accessing ${dir}: ${err.message}`);
    process.exit(1);
}

const visibleNames = [];

for(const entry of entries){
    if(!options.all && entry.name.startsWith(".")) continue;    
    visibleNames.push(entry.name);
}

if (options.all) {
  visibleNames.unshift(".", "..");
}
if(options.one){
    console.log(visibleNames.join("\n"));
} else{
    console.log(visibleNames.join("       "));
}