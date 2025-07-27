import { program } from "commander";
import{promises as fs} from "node:fs";
import process from "node:process";

program
.name("cat")
.description("displays the contents of a file")
.option('-n, --number', 'Number all output lines')
.argument("<filepath>");

program.parse();

const args = program.args

const path = args[0]
const content = await fs.readFile(path, "utf-8");
console.log(content)