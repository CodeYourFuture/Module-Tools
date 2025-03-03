#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt said by the Doctor.
# The output should contain 6 lines.

grep ^Doctor dialogue.txt # i tried to use the "" quotes but my terminal didnt accept that

Doctor: Hello
Doctor: What's wrong today?
Doctor: That sounds frustrating. When did this start?
Doctor: Say "Hi".
Doctor: You didn't say hello
Doctor: You're welcome, goodbye
