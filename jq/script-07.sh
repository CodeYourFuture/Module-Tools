#!/bin/bash

set -euo pipefail

# The input for this script is the scores.json file.
# Command to output just the names of each player along with the score from their last attempt.
#  output contains 6 lines, each with one word and one number on it.
# The first line is "Ahmed 4" with no quotes.

jq -r '.[] | .name + " " + (.scores[-1]|tostring)' scores.json