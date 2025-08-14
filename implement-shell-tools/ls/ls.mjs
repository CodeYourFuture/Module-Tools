import { program } from "commander"
import process from "node:process"
import { promises as fs } from "node:fs"
import { readdir } from 'node:fs/promises'

program
    .name("ls")
    .description("Lists the files in a directory")
    .option("-1, --one", "One per line")
    .option("-a", "Include files starting with dot")
    .argument("filepath")
program.parse(process.argv)

const argv = program.args
const opts = program.opts()

if (argv.length != 1){
    console.error("Expected 1 argument")
    process.exit(1)
}

const content = await fs.readdir(argv[0])

console.log(content.join(opts.one ? "\n": " "))
