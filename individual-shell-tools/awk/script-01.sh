#!/bin/bash

set -euo pipefail

# TODO: Write a command to output just the names of each player in `scores-table.txt`.
# Your output should contain 6 lines, each with just one word on it.

# awk splits each line into fields on whitespace; $1 is the first field (the player's name)
awk '{print $1}' scores-table.txt
