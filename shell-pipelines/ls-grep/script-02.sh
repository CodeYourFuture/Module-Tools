#!/bin/bash

set -euo pipefail

# TODO: Write a command to output the names of the files in the sample-files directory whose name starts with an upper case letter.
ls | grep '^[A-Z]'
# Your output should contain 10 files.
