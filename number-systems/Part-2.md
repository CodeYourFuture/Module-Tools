Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

The answers to these questions will require a bit of explanation, not just a simple answer.

Q16: How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
Answer:A binary number is a power of two if it has exactly one 1 and all the other digits are 0. For example 1000 (8) has one 1, but 110 (6) has two 1s, so 6 is not a power of two.

Q17: If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer:0x21 is 33 in decimal, and 33 in the ASCII table is the character !

Q18: If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer:0x21 is 33. In greyscale, 0 is black and 255 is white, so 33 is a very dark grey, almost black.

Q19: If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
Answer:AA = 170, 00 = 0, FF = 255. So the numbers are 170, 0, 255.

Q20: If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer:Red = 170, Green = 0, Blue = 255. Red and blue with no green makes purple, so it is a purple/violet colour.
