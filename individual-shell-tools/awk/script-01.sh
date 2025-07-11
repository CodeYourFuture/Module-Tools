#!/bin/bash

set -euo pipefail

# TODO: Write a command to output just the names of each player in `scores-table.txt`.
# Your output should contain 6 lines, each with just one word on it.

#Answer
cut -d' ' -f1  individual-shell-tools/awk/scores-table.txt
# cut to extract specific column from text and -d' ' sets the delimiter to a space and -f1 extract the first field.
