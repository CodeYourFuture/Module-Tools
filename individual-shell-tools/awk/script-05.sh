#!/bin/bash

set -euo pipefail

awk '($3 > 0) {attempt++} ($4 > 0) {attempt++} ($5 > 0) {attempt++} ($6 > 0) {attempt++} ($7 > 0) {attempt++} {print $1,attempt} attempt=0' scores-table.txt

# TODO: Write a command to output just the names of each player along with the number of times they've played the game.
# Your output should contain 6 lines, each with one word and one number on it.
# The first line should be "Ahmed 3".
