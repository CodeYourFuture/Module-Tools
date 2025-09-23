Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

Convert the decimal number 14 to binary.
Answer:  1110

Convert the binary number 101101 to decimal:
Answer:32,8,4,1 = 45

Which is larger: 1000 or 0111?
Answer: 1000 is larger since the left most digit is 1 compared to the other number.

Which is larger: 00100 or 01011?
Answer: 01011 is larger

What is 10101 + 01010?
Answer: 1111

What is 10001 + 10001?
Answer: 100010

What's the largest number you can store with 4 bits, if you want to be able to represent the number 0?

Answer1: If representing 0 means having 0000 AS A POSSIBLE NUMBER in the range of 0 to largest number produced by four digits, then the largest possible number is when all the digits are one which makes 1111 the largest number.

Answer2: If it means having 0 in one of the digits as a possible occurrence, then the largest possible number produced when zero goes to the last digit to have the least effect which  1110 the largest number.


How many bits would you need in order to store the numbers between 0 and 255 inclusive?
Answer: since 256 is 2^8 the biggest number of digits with 255 inclusive is made when we have  digits.

How many bits would you need in order to store the numbers between 0 and 3 inclusive?
Answer: 2 bits

How many bits would you need in order to store the numbers between 0 and 1000 inclusive?
Answer: 10 bits. since 2^n - 1 = the biggest number with n bits.

How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
Answer: only of it has only 1 bit as 1 and the rest are zeros

Convert the decimal number 14 to hex.
Answer: it is E

Convert the decimal number 386 to hex.
Answer: 281

Convert the hex number 386 to decimal.
Answer:6*(16^0)+8*(16^1)+3*(16^2) = 902

Convert the hex number B to decimal.
Answer: 11

If reading the byte 0x21 as a number, what decimal number would it mean?
Answer: 21hex = 2(16^1)+1(16^0) = 33

If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer: !

If reading the byte 0x21 as a gray scale colour, as described in "Approaches for Representing Colors and Images", what color would it mean?
Answer: Since hex21 is 33 in decimal and we have a range of 0(black) to 255(white) in decimal, then 33 is relatively close to zero. So it the gray scale it a dark grey

If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: Each set of  2 hex digits stands for each of primary colors in the following order:

RRGGBB: comparing it to AA00FF means that we don't have any greens. so we would have a mixture of blue and red. So eventually we have shade of purpule

If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
Answer: 170, 0 , 255
