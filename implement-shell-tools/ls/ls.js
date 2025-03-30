//note to myself:
// path.resolve() converts a relative path into an absolute path. 
//The last argument (dir) is resolved relative to the first argument.
//syntax: path.resolve(...paths);
//process.cwd() Returns the current working directory of the process (i.e., where the user ran the command from).It does NOT return the script’s directory.
//targetDir is created to store this resolved absolute path for reliable use in fs.readdirSync().
import  fs  from "fs/promises";
import { Command } from "commander";
import path from "path";

const program = new Command();

program
    .argument('[directory]', 'Directory to list', '.')//This specifies the directory argument. If no directory is provided, it defaults to the current directory (.)
    .option("-l, --format", "List files in a single column") // Add -1 flag
    .option("-a, --hidden", "Show hidden files (like ls -a)") // Add -a flag
    .action(async (directory) => {
        const resolvedPath = path.resolve(directory);
        
        const options = program.opts();
        
        try {
            const files = await fs.readdir(resolvedPath, { withFileTypes: true }); // files is an array of files inside the directory
            //{ withFileTypes: true } returns file objects, allowing you to filter out hidden files if needed.
        

            // If `-a` is NOT set, filter out hidden files (those starting with ".")
            let filteredFiles = files.map(file => file.name);

            if(!options.hidden){
                filteredFiles = filteredFiles.filter(file => !file.startsWith("."));
            }
            if(options.format){
                console.log(filteredFiles.join("\n"))// Print files in a single column (default `ls -1` behavior)
            }else{
                console.log(filteredFiles.join(" "))// Print files space-separated (default `ls` behavior)
            }
        } catch (error) {
            console.error(`Error reading directory: ${error.message}`);
            process.exit(1);
        }
    })

    program.parse(process.argv)








// async function readFile(directory) {
//     console.log("this is from inside the function")
//     try{
//         const files = await fs.readdir(directory);// Array of files in the directory
//         console.log("files -->", files)
//         console.log("files.join-->", files.join(' '))// String of files in the directory
//     } catch (error) {
//         console.error(`Error reading directory: ${error.message}`)
//         process.exit(1);
//     }
// }
// const directory = process.argv[2] || '.'
// console.log("directory-->", directory);
// readFile(directory)





// const program = new Command();

// program
//     .name("ls")
//     .description("writing a simple ls implementation using commander.js")

// program
//     .command("ls")
//     .description("lists files in the directory")
//     .argument("[directory]","Directory to list", ".")
//     .action((dir) => {
//         const targetDir = path.resolve(process.cwd(), dir);

//         console.log("targetDir-->", targetDir)
//         const files = fs.readdirSync(targetDir);
//         console.log("files -->", files?.join(" "));
//     }) 

//     program.parse();