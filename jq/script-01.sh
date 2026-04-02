#!/bin/bash

set -euo pipefail

# The input for this script is the person.json file.
# Command to output the name of the person.
# Output  is the string "Selma", but does not contain any quote characters.

jq -r '.name' person.json