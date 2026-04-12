import { program } from 'commander'
import process from 'process'
import fs from 'fs'

// const argv = process.argv[4]
// const data = fs.readFileSync(`sample-files/${argv}`, 'utf-8')

program
  .command('cat <file>')
  .description('Output file content')
  .option('-a, --all', 'Output all content')
  .option('-n, --line', 'Output each line with number')
  .option('-b, --nonempty', 'Output total lines not empty')
  .action((file, options) => {
    const data = fs.readFileSync(`sample-files/${file}`, 'utf-8').split('\n')
    if (options.all) {
      console.log(data.join())
    }
    if (options.line) {
      for (let i = 0; i < data.length; i++) {
        console.log(`${i} - ${data[i]}`)
      }
    }
    if (options.nonempty) {
      let totalline = 0
      data.forEach((line) => {
        if (line.length != 0) {
          totalline++
        }
      })
      console.log(totalline)
    }
  })

program.parse()
