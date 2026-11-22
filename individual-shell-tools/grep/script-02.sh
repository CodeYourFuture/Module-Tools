#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt that contains the word Doctor (regardless of case).
# The output should contain 9 lines.

# Both Doctor and doctor should match, even in the middle of a line.
grep -iw 'Doctor' dialogue.txt
