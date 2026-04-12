import { program } from 'commander'
import process from 'process'
import fs from 'fs'

const argv = process.argv[2]
const data = fs.readFileSync(`sample-files/${argv}`, 'utf-8')
program
  .command('cat')
  .description('Output file content')
  .option('-a, --all', "show all users' processes")
  .action(console.log(data))
