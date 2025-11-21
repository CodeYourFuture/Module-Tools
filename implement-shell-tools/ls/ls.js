import { program } from "commander";
import { promises as fs } from "node:fs";
import process from "node:process";

// configure the CLI program with its name, description, arguments, options, and actions (the help instructions)
program
    .name("ls")
    .description("An alternative to the 'ls' command")
    .argument("[directory]", "The directory to list")
    // Commander stores -1 as a string key that is accessed using options['1']
    .option("-1", "List all files, one per line")
    .option("-a, --all", "Include hidden files (those starting with .) in the listing")
    .action(async (directory, options) => {
      if (program.args.length > 1) {
          console.error(`Expected no more than 1 argument (sample-files) but got ${program.args.length}.`);
          process.exit(1);
      }

      // default directory to current folder
      directory = directory || ".";

      await newLs(directory, options['1'], options.all);
    });

program.parse(process.argv);



function sortEntries(entries) {
    // localeCompare = take into account rules of system language/region for ordering 
    // undefined = uses the system default, numeric = regular number sorting, base = ignore case & accents
    return entries.sort((a, b) => 
        a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' })
    );
}


async function newLs(directory, oneFlag, allFlag) {
    try {
        // check if the path exists
        const stats = await fs.stat(directory);

        // if it’s a file, just print its name
        if (stats.isFile()) {
            console.log(directory);
            return;
        } 

        // read directory contents
        const entries = await fs.readdir(directory);

        let finalEntries;
        
        // organize -a output (visible files (doesn't start with a .) and hidden files (starts with a .))
        const visibleFiles = entries.filter(name => !name.startsWith('.'));
        const hiddenFiles = entries.filter(name => name.startsWith('.') && name !== '.' && name !== '..');

        if (allFlag) {
            // add visible and hidden files to the new ['.', '..'] array literal
            finalEntries = ['.', '..']
                .concat(sortEntries(visibleFiles))
                .concat(sortEntries(hiddenFiles));
        } else {
            // return sorted array with visible files
            finalEntries = sortEntries(visibleFiles);
        }

        // organize -1 output
        if (oneFlag) {
            for (const entry of finalEntries) {
                console.log(entry);
            }
        } else {
            //no flags (separated by 2 spaces)
            console.log(finalEntries.join('  '));
        }

    } catch (err) {
        console.error(`ls: cannot access '${directory}': No such file or directory`);
    }
}



    
    
    
