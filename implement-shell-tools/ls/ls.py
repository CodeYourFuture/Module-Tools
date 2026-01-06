import argparse
import os
import stat
import pwd
import grp
import time

parser = argparse.ArgumentParser(
    prog="ls-command", description="ls shell command on python"
)

parser.add_argument("-1", action="store_true", dest="one", help="One file per line")
parser.add_argument(
    "-l", action="store_true", help="Display long format description files"
)
parser.add_argument(
    "-a", action="store_true", help="Display hidden files along with visible"
)
parser.add_argument("path", nargs="*", default=["."], help="The file to search")


args = parser.parse_args()


def long_format(path, file):
    info = os.stat(path)
    permissions = stat.filemode(info.st_mode)
    size_file = info.st_size
    owner = pwd.getpwuid(info.st_uid).pw_name
    group = grp.getgrgid(info.st_gid).gr_name
    mtime = time.strftime("%b %d %H:%M", time.localtime(info.st_mtime))
    print(permissions, size_file, owner, group, mtime, file)


for path in args.path:
    if os.path.isfile(path):
        file = os.path.basename(path)
        if args.l:
            long_format(path, file)
        else:
            print(file)
    elif os.path.isdir(path):
        files = os.listdir(path)

    if not args.a:
        files = [file for file in files if not file.startswith(".")]

    for file in files:
        full_file_path = os.path.join(path, file)

        if args.l:
            long_format(full_file_path, file)
        else:
            if args.one:
                print(file)
            else:
                print(file, "\n")
