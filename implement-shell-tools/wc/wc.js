import { program } from 'commander'
import fs from 'fs'
import { Buffer } from 'buffer'
import process from 'process'
program
  .command('wc <file>')
  .description('File word counts')
  .option('-l, --line', 'print the newline counts')
  .option('-w, --count', 'print the word counts')
  .option('-c, --bytes', 'print the bytes counts')
  .action((file, options) => {
    const content = fs.readFileSync(`sample-files/${file}`, 'utf-8')
    if (options.line) {
      console.log(content.split('\n').length)
    }
    if (options.bytes) {
      console.log(Buffer.from(content).toString('hex'))
    }
    if (options.count) {
      console.log(content.split(' ').length)
    }
    if (options.line && file == '*') {
      const files = fs.readdirSync('sample-files/', { withFileTypes: true })
      console.log(files)
    }
  })

program.parse()
