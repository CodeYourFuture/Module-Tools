#!/bin/bash

set -euo pipefail

# TODO: Write a command to output the number of lines in the file helper-files/helper-3.txt.
# The output should include the number 3. The output should not include the number 19.
path="/Users/cyf/Documents/SDC/Module-Tools/individual-shell-tools/helper-files/helper-3.txt"
wc -l "$path"