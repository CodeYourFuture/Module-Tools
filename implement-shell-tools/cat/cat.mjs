import { program } from "commander";  
import { promises as fs } from "node:fs";
import process from "node:process";

program
    .name("display-content-of-a-file")
    .description("cat is used to display the content of a file or print the content of a file.")
    .option('-n', 'number output lines')
    .option('-b', 'number non-empty output lines')
    .argument("<paths...>", "The file path/s to process"); //path as array of string

//this is what happen when run the comand
program.action(async (paths) => {
    const options = program.opts();  //get the selected options like -b
    let combinedData = "";
    for(const path of paths){ //loop through all file paths
        const data = await fs.readFile(path, "utf-8"); // read the file as text and add text to combined data
        combinedData += data + "\n";
    }
    //if user use -b option
    if(options.b){
        let lineNum = 1;
        const numberedPrint = combinedData
            .split('\n')
            .map(line => {
                if (line.trim() === ''){
                    return line; //if line is empty, return it with no number
                }
                else{
                    return `${(lineNum++).toString().padStart(6)} ${line}`;
                }
            })
            .join('\n'); //join the lines back into a full string
            process.stdout.write(numberedPrint + '\n'); //show result in the terminal
    }
    //if user used -n option
    else if(options.n){
        const numberedPrint = combinedData
            .split('\n')
            .map((line, i) => `${(i + 1).toString().padStart(6)} ${line}`)
            .join('\n');
        process.stdout.write(numberedPrint + '\n');
    }
    //if user didnt use -n or -b
    else{
        process.stdout.write(combinedData); //just print the text with no line numbers
    }  
});
program.parse(); //start the command