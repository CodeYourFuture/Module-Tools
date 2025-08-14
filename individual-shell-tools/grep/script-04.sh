#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt that does not contain the word "Hello" (regardless of case).
# The output should contain 10 lines.

grep hello -iv dialogue.txt

Doctor: What's wrong today?
Doctor: That sounds frustrating. When did this start?
Doctor: Say "Hi".
Patient: Hi
Patient: I seem to be cured!
Doctor: You're welcome, goodbye

Patient: I went to the doctor!
Spouse: I'm glad you saw the Doctor: did they cure you?
Patient: Yes!
