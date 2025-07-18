#!/bin/bash

set -euo pipefail

# TODO: Write a command to output the names of the files in the sample-files directory whose name starts with an upper case letter.
# Your output should contain 10 files.
path="/Users/cyf/Documents/SDC/Module-Tools/shell-pipelines/ls-grep/sample-files"
ls $path | grep '^[A-Z]'