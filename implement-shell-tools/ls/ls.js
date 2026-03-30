import { promises as fs } from "node:fs";
import { program } from "commander";

program
  .name("list files and directories")
  .option("-a", "show hidden files")
  .option("-1", "force displaying each item in a new line")
  .argument("<paths...>", "path of directory");

program.parse();

const showHiddenFiles = program.opts()["a"];
const showFilesInLines = program.opts()["1"];
const fetchedDirectories = await fetchDirectoriesFunc(program.args);

console.log(formatDisplay(fetchedDirectories));

function formatDisplay(fetchedDirectories) {
  const controlDisplaying = fetchedDirectories.map((directoryFilesInArray) => {
    const joiner = showFilesInLines ? `\n\r` : `  `;
    const showFolderName =
      fetchedDirectories.length > 1
        ? `${directoryFilesInArray.folderName}:\n\r`
        : "";

    return `${showFolderName}${directoryFilesInArray.files.join(joiner)}`;
  });
  return controlDisplaying.join("\n\r\n\r");
}

// returns array of objects, like: [{folderName: [file1, file2]}]
async function fetchDirectoriesFunc(directories) {
  const result = [];

  for (const folderName of directories) {
    let files = await fs.readdir(folderName);

    if (showHiddenFiles) files.unshift(".", "..");

    files.sort((a, b) => a.localeCompare(b));
    result.push({
      folderName,
      files,
    });
  }

  return result;
}
