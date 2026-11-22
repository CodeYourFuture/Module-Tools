#!/bin/bash

set -euo pipefail

# TODO: Write a command to output the name of every `.txt` file in this directory which contains a line of dialogue said by the Doctor.
# The output should contain two filenames.

# Keep the file order consistent across machines and print just the matching filenames.
export LC_ALL=C
grep -l '^Doctor:' *.txt
