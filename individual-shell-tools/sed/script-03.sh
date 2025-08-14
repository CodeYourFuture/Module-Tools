#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt removing any line which contains a number.
# The output should contain 6 lines.
path="/Users/cyf/Documents/SDC/Module-Tools/individual-shell-tools/sed/input.txt"
sed "/[0-9]/d" $path