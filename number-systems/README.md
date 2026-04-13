Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

Convert the decimal number 14 to binary.
Answer: 14 ÷ 2 → remainders: 1110

Convert the binary number 101101 to decimal:
Answer: 1·32 + 0·16 + 1·8 + 1·4 + 0·2 + 1·1 = 32 + 8 + 4 + 1 = 45

Which is larger: 1000 or 0111?
Answer: 1000 (1000 = 8, 0111 = 7)

Which is larger: 00100 or 01011?cd
Answer: 01011 (00100 = 4, 01011 = 11)

What is 10101 + 01010?
Answer: 11111 (21 + 10 = 31 → binary: 11111)

What is 10001 + 10001?
Answer: 100010 (17 + 17 = 34 → binary: 100010)

What's the largest number you can store with 4 bits, if you want to be able to represent the number 0?
Answer: 2⁴ − 1 = 15

How many bits would you need in order to store the numbers between 0 and 255 inclusive?
Answer: 8 bits (256 values → 2⁸)

How many bits would you need in order to store the numbers between 0 and 3 inclusive?
Answer: 2 bits (4 values → 2²)

How many bits would you need in order to store the numbers between 0 and 1000 inclusive?
Answer: 10 bits (2⁹ = 512 (too small), 2¹⁰ = 1024)

How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
Answer: Only one 1 bit (or n & (n−1) = 0)  (It has exactly one ‘1’ bit (e.g., 1000). Or use: n & (n − 1) = 0 (for n > 0))

Convert the decimal number 14 to hex.
Answer: E (14 = E)

Convert the decimal number 386 to hex.
Answer: 182 (386 ÷ 16 → 182 → 1 → remainders → 182₁₀ = 182? (correct breakdown:) 386 = 1×256 + 8×16 + 2 → 182₁₆)

Convert the hex number 386 to decimal.
Answer: 902 (3×256 + 8×16 + 6 = 768 + 128 + 6 = 902)

Convert the hex number B to decimal.
Answer: 11 (B = 11)

If reading the byte 0x21 as a number, what decimal number would it mean?
Answer: 33 (2×16 + 1 = 33)

If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer: ! (ASCII 33 = !)

If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: Dark Grey (33/255 → very dark grey)

If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: Purple/magenta-like (R=170, G=0, B=255 → purple/magenta)

If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
Answer: 170, 0, 255 (AA = 170, 00 = 0, FF = 255)
.