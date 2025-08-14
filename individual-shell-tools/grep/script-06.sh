#!/bin/bash

set -euo pipefail

# TODO: Write a command to output the name of every `.txt` file in this directory which contains a line of dialogue said by the Doctor.
# The output should contain two filenames.
path="/Users/cyf/Documents/SDC/Module-Tools/individual-shell-tools/grep"
grep -l '^Doctor:' "$path"/*.txt 