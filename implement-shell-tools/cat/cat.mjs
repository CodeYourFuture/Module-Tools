import { program } from "commander";
import{promises as fs} from "node:fs";
import process from "node:process";

program
.name("cat")
.description("displays the contents of a file")
.option('-n, --number', 'Number all output lines')
.option("-b, --number-nonblank", 'Number non-blank output lines only')
.argument("<filepath>");

program.parse();


const args = program.args;
const opts = program.opts();

if (args.length === 0) {
  console.error("Error: Missing <filepath> argument.");
  program.help();
}

const path = args[0]
const content = await fs.readFile(path, "utf-8");
 const lines = content.split('\n');
if(opts.number){
     for (let i = 0; i < lines.length; i++) {
        console.log(`${i + 1}\t${lines[i]}`);
      }
    }else if (opts.numberNonblank) {
      let lineNumber = 1;
      for (let i = 0; i < lines.length; i++) {
        if (lines[i].trim() !== '') {
          console.log(`${lineNumber.toString().padStart(6)}\t${lines[i]}`);
          lineNumber++;
        }
     }
    }else console.log(content)
    
    