#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt with one change:
# If a line starts with a number and a space, make the line instead end with a space and the number.
# So line 6 which currently reads "37 Alisha" should instead read "Alisha 37".
# The output should contain 11 lines.

# -E enables extended regex so ( ) create capture groups without backslashes
# ^([0-9]+) captures the number at the start of the line, (.*) captures the rest,
# and \2 \1 writes them back in swapped order with a space between
sed -E "s/^([0-9]+) (.*)/\2 \1/" input.txt
