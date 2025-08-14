#!/bin/bash

set -euo pipefail

# The input for this script is the events.txt file.
# Command to show how many times anyone has entered and exited.
# It should be clear from your script's output that there have been 5 Entry events and 4 Exit events.

sort events.txt | uniq -c