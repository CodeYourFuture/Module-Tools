Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

The answers to these questions will require a bit of explanation, not just a simple answer.

Q16: How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?

when the numbers of zeroes and ones are the same?

Answer: It has to either be 1 in binary or 1 followed by however many zeroes. For example 1000, 1, 10 are all a power of two

Q17: If reading the byte 0x21 as an ASCII character, what character would it mean?
0b - binary
0x - hexadecimal

I looked up the ascii table and it was !

Answer: !

Q18: If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?

Answer: Should be somewhere between completely black and dark grey as the value is 33

Q19: If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?

FF = 15*16^1 + 15*16^0
AA = 10*16^1 + 10*16^0

AA 00 FF
170 0 255

Answer: 170 0 255

Q20: If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?

170/255*100 = 66
0/255*100 = 0
255/255*100 = 100

Answer: 66% Red, 0% Green and 100% Blue so its purple
