#!/bin/bash

set -euo pipefail

# The input for this script is the scores.json file.
# Command to output just the names of each player along with the total scores from all of their games added together.
# Output contains 6 lines, each with one word and one number on it.
# The first line is "Ahmed 15" with no quotes.

jq -r '.[] | .name + " " + ((.scores | add)|tostring)' scores.json
