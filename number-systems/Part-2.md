Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

The answers to these questions will require a bit of explanation, not just a simple answer.

Q16: How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
Answer: If the binary number has only one bit value of 1, and the rest are values of 0, then it is a power of two. The value of 1 represent 1 multiplied by a 2 to the power of the corresponding position index (0,1,....).

Q17: If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer: The hexadecimal value of 21 correspond to the binary value of 00100001, which is the exclamation mark.

Q18: If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: It would be a very dark grey colour because it is close to 0x00 which is black.

Q19: If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
Answer: 170, 0, 255 ==> 0xAA -> 170, 0x00 -> 0, 0xFF -> 255. On byte is represented by 2 hexadecimal values in the sequence.

Q20: If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: again, we would have a RGB(170, 0, 255), that is quite a lot of red, no green and full value of blue - it would be light purple.
