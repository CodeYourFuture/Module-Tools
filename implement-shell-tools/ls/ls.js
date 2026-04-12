import { program } from 'commander'
import process from 'process'
import fs from 'fs'
program
  .command('ls')
  .description('Output available files on directory')
  .option('-a, --all', 'Output all files')
  .option('-1, --line', 'List one file per line')
  .action((options) => {
    const contents = fs.readdirSync(process.cwd(), { withFileTypes: true })

    if (options.all) {
      contents.forEach((content) => {
        console.log(content.name)
      })
    }
    if (options.line) {
      console.log(contents[0].name)
    }
  })

program.parse()
