#!/bin/bash

set -euo pipefail

# TODO: Write a command to output just the names of each player in `scores-table.txt`.
# Your output should contain 6 lines, each with just one word on it.

cd individual-shell-tools/awk
awk '{print $1}' scores-table.txt
