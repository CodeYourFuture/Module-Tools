#!/bin/bash

set -euo pipefail

# Command to output the names of the files in the sample-files directory whose name starts with an upper case letter.
# Your output should contain 10 files.

ls sample-files | grep '^[A-Z]'