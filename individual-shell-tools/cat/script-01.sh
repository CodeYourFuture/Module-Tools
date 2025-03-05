#!/bin/bash

set -euo pipefail

# TODO: Write a command to output the contents of the helper-1.txt file inside the helper-files directory to the terminal.
# The output of this command should be "Once upon a time...".



# method 1 (relative path)
cat ../helper-files/helper-1.txt

# method 2
cd ../helper-files/
cat helper-1.txt 

# method 3 (absolute path)
cat /Users/samira/Desktop/CYF/SDC/Module-Tools/individual-shell-tools/helper-files/helper-1.txt
