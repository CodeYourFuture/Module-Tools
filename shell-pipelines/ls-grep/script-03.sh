#!/bin/bash

set -euo pipefail
ls -1 sample-files | grep '^[A-Z]' | grep -v '.*[A-Z].*[A-Z]'
# TODO: Write a command to output the names of the files in the sample-files directory whose name starts with an upper case letter and doesn't contain any other upper case letters.
# Your output should contain 7 files.

