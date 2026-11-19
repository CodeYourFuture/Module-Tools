#!/bin/bash

set -euo pipefail

# TODO: Write a command to output the contents of the helper-1.txt file inside the helper-files directory to the terminal.
# The output of this command should be "Once upon a time...".

# Use ../ because helper-files is next to the cat directory.
cat ../helper-files/helper-1.txt
