Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

The answers to these questions should be a number, either in binary, hex, or decimal.

Q1: Convert the decimal number 14 to binary.
Answer: 1110

Q2: Convert the binary number 101101 to decimal:
Answer: 45

Q3: Which is larger: 1000 or 0111?
Answer: 1000

I compared the bits from the left. The first bit is already different: 1000 has a 1 there and 0111 has a 0, so 1000 is bigger.

Q4: Which is larger: 00100 or 01011?
Answer: 01011

Both numbers start with 0. The next digit is 1 in 01011 and 0 in 00100, so 01011 is bigger.

Q5: What is 10101 + 01010?
Answer: 11111

Each column has one 1 and one 0, so every column gives 1 and there are no carries.

Q6: What is 10001 + 10001?
Answer: 100010

The rightmost 1 + 1 gives 0 and carries 1 into the next column. The two leftmost 1s also give 0 and carry 1 into a new column.

Q7: What's the largest number you can store with 4 bits, if you want to be able to represent the number 0?
Answer: 15

Four bits give 2 x 2 x 2 x 2 = 16 possible patterns. Counting from 0, the last value is 15, represented by 1111.

Q8: How many bits would you need in order to store the numbers between 0 and 255 inclusive?
Answer: 8

Eight bits give 256 different patterns, enough for every number from 0 through 255.

Q9: How many bits would you need in order to store the numbers between 0 and 3 inclusive?
Answer: 2

Two bits give four patterns: 00, 01, 10, and 11.

Q10: How many bits would you need in order to store the numbers between 0 and 1000 inclusive?
Answer: 10

Nine bits give 512 patterns. Ten bits give 1024, enough for all 1001 values from 0 through 1000.

Q11: Convert the decimal number 14 to hex.
Answer: E

Hex uses A through F for the values 10 through 15, so 14 is E.
 
Q12: Convert the decimal number 386 to hex.
Answer: 182

386 is one group of 256, eight groups of 16, and two ones. Those are the three hex digits.

Q13: Convert the hex number 386 to decimal.
Answer: 902

The digits are worth 3 × 256, 8 × 16, and 6 × 1. Adding 768, 128, and 6 gives 902.

Q14: Convert the hex number B to decimal.
Answer: 11

In hex, A is 10 and B is the next digit, so B is 11.

Q15: If reading the byte 0x21 as a number, what decimal number would it mean?
Answer: 33

The 2 is in the sixteens place and the 1 is in the ones place. That gives 32 + 1 = 33.

Q16: Continues in Part-2
