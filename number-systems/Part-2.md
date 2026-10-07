Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

The answers to these questions will require a bit of explanation, not just a simple answer.

Q16: How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
Answer: A binary number is a power of two if it has exactly one 1 bit and all other bits are 0. For example: 100 000 only has only 1 bit so power of two, 2⁵. 
        However 100 100  has two one bits  so not power of two instead  2⁵+ 2²

Q17: If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer:0x21 convert to binary number: 0b0010001 which represents ! character in ASCII program

Q18: If reading the byte 0x21 as a greyscale color, as described in "Approaches for Representing Colors and Images", what color would it mean?
Answer: due to that 0x00=black 0xFF=white, ox21 should be low value(33 out of 255 in decimal value) so it should be dark grey(almost dark)

Q19: If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
Answer: AA=160(16*10+10=170),00=00, FF=255(16*15+15=255) and also two hexadecimal number is one-byte binary number, so 0xAA00FF as a sequence of three one-byte
        decimal numbers are 170,0,255

Q20: If reading the bytes 0xAA00FF as an RGB color, as described in "Approaches for Representing Colors and Images", what color would it mean?
Answer: As red = 0xAA = 170,Green = 0x00 = 0,Blue = 0xFF = 255 so RGB(170, 0, 255) so it shows strong red component,no green and strong blue component.
        The color should be a bright purple / magenta color.

