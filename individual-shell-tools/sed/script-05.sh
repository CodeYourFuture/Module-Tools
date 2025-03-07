#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt with one change:
# If a line starts with a number and a space, make the line instead end with a space and the number.
# So line 6 which currently reads "37 Alisha" should instead read "Alisha 37".
# The output should contain 11 lines.

sed 's/^\([0-9]\+\) \(.*\)$/\2 \1/' input.txt

# \([0-9]\+\ - matches one or more digits.
# \(.*\)$/\2 \1/ - matches the rest of the line (2 - part after digit, 1 - part with digit).