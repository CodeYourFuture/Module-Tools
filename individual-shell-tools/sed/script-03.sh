#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt removing any line which contains a number.
# The output should contain 6 lines.

# /[0-9]/ selects lines containing a digit and the d command deletes those lines from the output
sed "/[0-9]/d" input.txt
