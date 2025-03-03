#!/bin/bash

set -euo pipefail

# TODO: Write a command to output, for each `.txt` file in this directory, how many lines of dialogue the Doctor has.
# The output should show that dialogue.txt contains 6 lines, dialogue-2.txt contains 2, and dialogue-3.txt contains 0.

grep ^Doctor -c *.txt # this command gaves the expected output

dialogue.txt:6
dialogue-2.txt:2
dialogue-3.txt:0

grep ^ Doctor -c *.txt # however here i put a space between the carrot and the search name and it gave me a different output, and i dont know why

grep: Doctor: No such file or directory
dialogue.txt:15
dialogue-2.txt:4
dialogue-3.txt:3
