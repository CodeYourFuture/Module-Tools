#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt replacing every occurrence of the string "We'll" with "We will".
# The output should contain 11 lines.
path="/Users/cyf/Documents/SDC/Module-Tools/individual-shell-tools/sed/input.txt"
old="We'll"
new="We will"
sed "s/$old/$new/g" $path