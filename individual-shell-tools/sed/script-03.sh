#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt removing any line which contains a number.
# The output should contain 6 lines.

sed -e '/[0-9]/d' input.txt # my output is only 4 lines instead of 6

This is a sample file for experimenting with sed.

It contains many lines, and there are some things you may want to do with each of them.       

We'll include some score information:
