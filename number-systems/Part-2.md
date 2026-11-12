Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

The answers to these questions will require a bit of explanation, not just a simple answer.

Q16: How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
Answer: A binary number is a power of two only if it has exactly one 1 digit, and all the other digits are 0. This is because each place value is a power of two, so one 1 means the number is just that power. Two or more 1s add powers together (like 8 + 2 = 10), which is not a power of two.

Q17: If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer: 0x21 is 33 in decimal. In the ASCII table, 33 is the character "!".

Q18: If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: 0x21 is 33 in decimal. In greyscale, 0 is black and 255 is white. 33 is close to 0, so it is a dark grey (almost black).

Q19: If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
Answer: Split 0xAA00FF into three bytes: AA, 00, FF. AA = 10 × 16 + 10 = 170, 00 = 0, FF = 15 × 16 + 15 = 255. So the numbers are 170, 0, 255.

Q20: If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: Read 0xAA00FF as three bytes: R = AA = 170, G = 00 = 0, B = FF = 255. That’s lots of red, no green and full blue, so the colour is purple (a bluish purple / violet).
