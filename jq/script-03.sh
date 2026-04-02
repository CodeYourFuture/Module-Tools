#!/bin/bash

set -euo pipefail

# The input for this script is the person.json file.
# Command to output the name of the person, then a comma, then their profession.
# Output is the string "Selma, Software Engineer", but does not contain any quote characters.

jq -r '.name + ", " + .profession' person.json