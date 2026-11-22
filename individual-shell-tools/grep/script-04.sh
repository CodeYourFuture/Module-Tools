#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt that does not contain the word "Hello" (regardless of case).
# The output should contain 10 lines.

# Flip the match with -v so lines with either Hello or hello are left out.
grep -ivw 'Hello' dialogue.txt
