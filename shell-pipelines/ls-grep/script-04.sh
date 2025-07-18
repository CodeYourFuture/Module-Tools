#!/bin/bash

set -euo pipefail
ls -1 sample-files | grep '^[A-Z]' | grep -v '.*[A-Z].*[A-Z]' | wc -l
# TODO: Write a command to count the number of files in the sample-files directory whose name starts with an upper case letter and doesn't contain any other upper case letters.
# Your output should be the number 7.
