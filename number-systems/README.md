Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

Convert the decimal number 14 to binary.
Answer: 1110

Convert the binary number 101101 to decimal:
Answer: 32+8+4+1 = 45

Which is larger: 1000 or 0111?
Answer: 1000

Which is larger: 00100 or 01011?
Answer: 01011

What is 10101 + 01010?
Answer: 11111

What is 10001 + 10001?
Answer: 100010

What's the largest number you can store with 4 bits, if you want to be able to represent the number 0?
Answer: 15

How many bits would you need in order to store the numbers between 0 and 255 inclusive?
Answer: 2^8 = 255 so 8 bits

How many bits would you need in order to store the numbers between 0 and 3 inclusive?
Answer: 2^2=4 2 bits
How many bits would you need in order to store the numbers between 0 and 1000 inclusive?
Answer: 2^10 = 1024 so 10 bits

How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
Answer: It's a power of 2 when it had only one 1

Convert the decimal number 14 to hex.
Answer: E

Convert the decimal number 386 to hex.
Answer: 182

Convert the hex number 386 to decimal.
Answer: 3*16^2 + 8*16^1 + 6*16^0 = 902

Convert the hex number B to decimal.
Answer: 11

If reading the byte 0x21 as a number, what decimal number would it mean?
Answer: 2×16^1 + 1×16^0 33

If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer: Should be converted to Decimal then ASCII code 33 : !

If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: A very dark grey (almost black), because 0 = black, 255 = white, and 33 is very low in (0-255)

If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: Purple , because no green, and full blue

If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
Answer: AA = 170
00 = 0
FF = 255
