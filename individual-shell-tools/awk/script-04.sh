#!/bin/bash

set -euo pipefail

# TODO: Write a command to output just the names of each player in $2London along with the score from their last attempt.
# Your output should contain 3 lines, each with one word and one number on it.
# The first line should be "Ahmed 4".

cd individual-shell-tools/awk
awk '/London/ {print $1, $NF}' scores-table.txt
