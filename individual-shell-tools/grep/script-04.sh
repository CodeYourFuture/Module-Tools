#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt that doesn't contain the word "Hello" (regardless of case).
# The output should contain 10 lines.
grep -v -i "hello" dialogue.txt
