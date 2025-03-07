#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt that does not contain the word "Hello" (regardless of case).
# The output should contain 10 lines.

grep -i -v "Hello" dialogue.txt

# -v - inverts, return lines that don't contain "Hello" or "hello"