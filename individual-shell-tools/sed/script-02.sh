#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt with numbers removed.
# The output should contain 11 lines.
# Line 6 of the output should be " Alisha".

# [0-9] matches any single digit; replacing it with nothing (//) deletes it, and g removes every digit on the line
sed "s/[0-9]//g" input.txt
