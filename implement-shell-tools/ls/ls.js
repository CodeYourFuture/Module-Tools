import {program} from "commander";
import process from "node:process";
import {promises as fs } from "node:fs";


program
.name ("list command clone")
.description("List all files & folders within current folder")
.argument("[directory]","Directory to list",".")
.option("-1","list file line by line")
.action(async (directory,options) =>
{
    try 
    {
        let files = await fs.readdir(directory);
        console.log(files.join(" "));
    }

    catch (error)
    {
        console.error('No such file or directory');
        process.exit(1);
    }

});

program.parse(process.argv);