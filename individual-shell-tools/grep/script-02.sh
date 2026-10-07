#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt that contains the word Doctor (regardless of case).
# The output should contain 9 lines.

cd individual-shell-tools/grep
grep -i "Doctor" dialogue.txt
