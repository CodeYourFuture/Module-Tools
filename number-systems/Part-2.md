Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

The answers to these questions will require a bit of explanation, not just a simple answer.

Q16: How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
Answer: I just count the `1`s. If there’s exactly one, it’s a power of two. `1000` has one `1`, so it counts. `1010` has two, so it doesn’t...

Q17: If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer: An exclamation mark (!).

The hex value 0x21 is 33 in decimal and ASCII is a table that assigns a character to each code number, and code 33 is the exclamation mark.

Q18: If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: Probably a very dark grey.

In 8-bit greyscale, 0 means black and 255 means white. The value 0x21 is 33, which is much closer to 0 than to 255. That puts it near the black end of the scale...

Q19: If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
Answer: 170, 0, and 255.

Each pair of hex digits is one byte, so split 0xAA00FF into AA, 00, and FF. A is 10, so AA is 10 x 16 + 10 = 170. The middle byte is 0. F is 15, so FF is 15 x 16 + 15 = 255.

Q20: If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: A nice vivid purple.

RGB reads the three bytes in red, green, blue order. That gives red 170, green 0, and blue 255. Red and blue together make purple, and the stronger blue gives it a bluish tint.
