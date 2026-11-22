#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt said by the Doctor.
# The output should contain 6 lines.

# Match Doctor: at the start of the line to find the lines spoken by the Doctor.
grep '^Doctor:' dialogue.txt
