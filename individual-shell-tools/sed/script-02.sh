#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt with numbers removed.
# The output should contain 11 lines.
# Line 6 of the output should be " Alisha".

# Replace each digit with nothing so the rest of the line stays as it is.
sed 's/[[:digit:]]//g' input.txt
