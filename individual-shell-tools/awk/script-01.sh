#!/bin/bash

set -euo pipefail

# TODO: Write a command to output just the names of each player in `scores-table.txt`.
# Your output should contain 6 lines, each with just one word on it.

# The name comes first on every row, so $1 is all we need.
awk '{print $1}' scores-table.txt
