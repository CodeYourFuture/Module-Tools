#!/bin/bash

set -euo pipefail

# TODO: Write a command to output the names of the files in the sample-files directory whose name starts with an upper case letter.
# Your output should contain 10 files.
ls -1 ./sample-files | grep '^[A-Z]'
ls -1 ./sample-files | grep '^[A-Z]' | wc -l