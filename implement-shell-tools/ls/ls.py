import os
import argparse
import locale


#set locale to the machine default setting
locale.setlocale(locale.LC_ALL, '')


parser = argparse.ArgumentParser(
    prog="ls",
    description="An alternative to the 'ls' command",
)

parser.add_argument("directory", nargs="?", default=".", help="The directory to list (defaults to the current directory)")
parser.add_argument("-1", "--single-column", action="store_true", help="List all files, one per line")
parser.add_argument("-a", "--all", action="store_true", help="Include hidden files (those starting with .) in the listing")

args = parser.parse_args()

# check if path exists 
if not os.path.exists(args.directory):
    print(f"ls: cannot access '${args.directory}': No such file or directory")
    exit(1)

# check if path is a directory
if os.path.isdir(args.directory):
    entries = os.listdir(args.directory)

    # if -a flag set
    if args.all:
        entries.extend(['.', '..'])

    # filter hidden files if -a (all) flag not set
    if not args.all:
        entries = [entry for entry in entries if not entry.startswith(".")]

    # sort the entries using locale-aware comparison
    entries.sort(key =locale.strxfrm)

    # print entries
    if args.single_column:
        for entry in entries:
            print(entry)
    else:
        print("  ".join(entries))











#     .argument("[directory]", "The directory to list")
#     // Commander stores -1 as a string key that is accessed using options['1']
#     .option("-1", "List all files, one per line")
#     .option("-a, --all", "Include hidden files (those starting with .) in the listing")
#     .action(async (directory, options) => {
#         try {
#             // default to current directory if none is specified
#             const dir = directory || ".";

#             await newLs(dir, options['1'], options.all);
#         } catch (err) {
#             console.error(`Error: ${err.message}`);
#         }
#     });

# program.parse(process.argv);


# // filter files based on visibility (includeHidden = true includes all files)
# function filterFiles(entries, includeHidden) {
#     return entries.filter(name =>
#         includeHidden ? true : !name.startsWith(".")
#     );
# }

# // sort entries: directories first, then files,
# function sortEntries(entries) {
#     const dirs = entries.filter(entry => {
#         try {
#             return fs.statSync(entry).isDirectory();
#         } catch (err) {
#             return false;
#         }
#     });

#     const files = entries.filter(entry => {
#         try {
#             return fs.statSync(entry).isFile();
#         } catch (err) {
#             return false;
#         }
#     });
#     // localeCompare = take into account rules of system language/region for ordering 
#     // undefined = uses the system default, numeric = regular number sorting, base = ignore case & accents
#     return entries.sort((a, b) =>
#         a.localeCompare(b, undefined, { numeric: true, sensitivity: "base" })
#     );
# }


# // print entries either one per line (-1 flag)
# function printEntries(entries) {
#     entries.forEach(entry => console.log(entry));
# }


# async function newLs(directory, oneFlag, allFlag) {
#     try {
#         // check if path exists and determine if file or directory
#         const stats = await fs.stat(directory);
        
#         // if a file, just print the name
#         if (stats.isFile()) {
#             console.log(directory);
#             return;
#         }

#         // reads directory contents 
#         const entries = await fs.readdir(directory);

#         // Filter out hidden files if no -a flag
#         const filteredEntries = filterFiles(entries, allFlag);

#         // Sort the entries using the sortEntries helper
#         const sortedEntries = sortEntries(filteredEntries);
        
#         // print entries for -1 flag (one per line)
#         printEntries(sortedEntries);
#     } catch (err) {
#         console.error(`ls: cannot access '${directory}': ${err.message}`);
#     }
# }