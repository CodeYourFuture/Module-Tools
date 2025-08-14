#!/bin/bash

set -euo pipefail

# TODO: Write a command to output just the names of each player in London along with the score from their last attempt.
# Your output should contain 3 lines, each with one word and one number on it.
# The first line should be "Ahmed 4".
awk '/London/ { if (NF<5) print $1, $NF; else print $1, $5}' scores-table.txt