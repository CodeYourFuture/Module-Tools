import process from "node:process";
import { promises as fs } from "node:fs";
import path from "node:path";

const arrArgv = process.argv.slice(2);

const longFormat = arrArgv.includes("-l");
const showHidden = arrArgv.includes("-a");

let paths = arrArgv.filter((argv) => !argv.startsWith("-"));
if (paths.length === 0) paths = ["."];

const printWholeList = (stats, name) => {
  const permissions = (stats.mode & 0o777).toString(8);
  const sizeFile = stats.size;
  const owner = stats.uid;
  const group = stats.gid;
  const timeMod = stats.mtime.toLocaleString();

  console.log(
    `${permissions}, ${owner}, ${group}, ${sizeFile}, ${timeMod}, ${name}`
  );
};
for (const listFile of paths) {
  const status = await fs.stat(listFile);
  if (status.isFile()) {
    if (longFormat) {
      printWholeList(status, listFile);
    } else {
      console.log(listFile);
    }
  } else {
    let files = await fs.readdir(listFile, { withFileTypes: true });

    if (!showHidden) {
      files = files.filter((file) => !file.name.startsWith("."));
    }

    for (const file of files) {
      const wholePath = path.join(listFile, file.name);

      if (longFormat) {
        const statusFile = await fs.stat(wholePath);
        printWholeList(statusFile, file.name);
      } else {
        console.log(file.name);
      }
    }
  }
}
