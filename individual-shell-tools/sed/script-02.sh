#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt with numbers removed.
# The output should contain 11 lines.
# Line 6 of the output should be " Alisha".

echo "removing numbers:"

sed 's/[0-9]//g' input.txt