#!/bin/bash

set -euo pipefail

# TODO: Write a command to output the number of lines in dialogue.txt that contain the word Doctor (regardless of case).
# The output should be exactly the number 9.

grep -i "Doctor" dialogue.txt | wc -l

# | - pipe, takes output from the first command and send it to the next command.