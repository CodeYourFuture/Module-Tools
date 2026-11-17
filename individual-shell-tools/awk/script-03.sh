#!/bin/bash

set -euo pipefail

# TODO: Write a command to output just the names of each player along with the score from their first attempt.
# Your output should contain 6 lines, each with one word and one number on it.
# The first line should be "Ahmed 1".

# $3 is the third field, which is the score from the player's first attempt
awk '{print $1, $3}' scores-table.txt
