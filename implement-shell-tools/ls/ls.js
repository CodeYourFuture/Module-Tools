import process from "node:process";
import { promises as fs } from "node:fs";
import path from "node:path";

const arrArgv = process.argv.slice(2);

const longFormat = arrArgv.includes("-l");
const showHidden = arrArgv.includes("-a");

const paths = arrArgv.filter((argv) => !argv.startsWith("-"));
if (paths.length === 0) path = "[.]";

for (let listFile of paths) {
  const status = await fs.stat(listFile);

  if (status.isFile()) {
    const permissions = (status.mode & 0o777).toString(8);
    const sizeFile = status.size;
    const owner = status.uid;
    const group = status.gid;
    const timeMod = status.mtime.toLocaleString();

    if (longFormat) {
      console.log(
        `${permissions}, ${owner}, ${group}, ${sizeFile}, ${timeMod}, ${listFile}`
      );
    } else {
      console.log(listFile);
    }
  } else {
    let files = await fs.readdir(listFile, { withFileTypes: true });

    if (!showHidden) {
      files = files.filter((file) => !file.name.startsWith("."));
    }

    for (let file of files) {
      const wholePath = path.join(listFile, file.name);
      const statusFile = await fs.stat(wholePath);

      const permissions = (statusFile.mode & 0o777).toString(8);
      const sizeFile = statusFile.size;
      const owner = statusFile.uid;
      const group = statusFile.gid;
      const timeMod = statusFile.mtime.toLocaleString();

      if (longFormat) {
        console.log(
          `${permissions}, ${owner}, ${group}, ${sizeFile}, ${timeMod}, ${file.name}`
        );
      } else {
        console.log(file.name);
      }
    }
  }
}
