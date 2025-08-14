import {program} from "commander";
import {promises as fs} from "node:fs";

program
  .name("ls")
  .description("List all the files in a directory")
  .option("-a, --all", "Include hidden files")
  .option("-1", "One entry per line")
  .argument("[dir]", "directory to list", ".");

program.parse();

const options = program.opts();
const dir = program.args[0] || ".";

const entries = await fs.readdir(dir, { withFileTypes: true });

const visibleNames = [];

for(const entry of entries){
    if(!options.all && entry.name.startsWith(".")) continue;    
    visibleNames.push(entry.name);
}

if(options["1"]){
    console.log(visibleNames.join("\n"));
} else{
    console.log(visibleNames.join("       "));
}
