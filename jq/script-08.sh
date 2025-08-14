#!/bin/bash

set -euo pipefail

# The input for this script is the scores.json file.
# Command to output just the names of each player along with the number of times they've played the game.
# output contains 6 lines, each with one word and one number on it.
# The first line is "Ahmed 3" with no quotes.

jq -r '.[] | .name + " " + ((.scores | length)|tostring)' scores.json