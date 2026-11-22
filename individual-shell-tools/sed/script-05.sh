#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt with one change:
# If a line starts with a number and a space, make the line instead end with a space and the number.
# So line 6 which currently reads "37 Alisha" should instead read "Alisha 37".
# The output should contain 11 lines.

# Grab the number and the text separately so 37 Alisha becomes Alisha 37.
sed -E 's/^([[:digit:]]+) (.*)$/\2 \1/' input.txt
