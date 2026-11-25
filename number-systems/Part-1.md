Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

The answers to these questions should be a number, either in binary, hex, or decimal.

Q1: Convert the decimal number 14 to binary.

8 4 2 1
1 1 1 0

8+4+2=14

Answer: 1110

Q2: Convert the binary number 101101 to decimal:

32 16 8 4 2 1
1 0 1 1 0 1

32+8+4+1=45

Answer: 45

Q3: Which is larger: 1000 or 0111?

8 4 2 1
1 0 0 0 = 8
0 1 1 1 = 7

Answer: 1000

Q4: Which is larger: 00100 or 01011?

16 8 4 2 1
0 0 1 0 0 = 4
0 1 0 1 1 = 8+2+1 = 11

Answer: 01011

Q5: What is 10101 + 01010?

16 8 4 2 1
1 0 1 0 1
0 1 0 1 0
=========

1 1 1 1 1

16+8+4+2+1=31

Answer: 11111

Q6: What is 10001 + 10001?

32 16 8 4 2 1
0 1 0 0 0 1
0 1 0 0 0 1
1 0 0 0 1 0

32+2=34

Answer: 100010

Q7: What's the largest number you can store with 4 bits, if you want to be able to represent the number 0?

Answer: The largest number is 1111 or 15. To represent 0 you would use 0000

Q8: How many bits would you need in order to store the numbers between 0 and 255 inclusive?

you need to find a number that produces less than 255 in this formula 2^n+1

so for this we'd use 2^8 which gives us 256

Answer: 8 bits

Q9: How many bits would you need in order to store the numbers between 0 and 3 inclusive?

two bits using the previous formula

Answer: 2

Q10: How many bits would you need in order to store the numbers between 0 and 1000 inclusive?

Answer: 10

Q11: Convert the decimal number 14 to hex.

Answer: E

Q12: Convert the decimal number 386 to hex.

386/16=24 remainder 2
24/16=1 remainder 8
1/16=0 remiander 1

Answer: 182

Q13: Convert the hex number 386 to decimal.

3*16^2 + 8*16^1 + 6*16^0 = 768+128+6= 902

Answer: 902

Q14: Convert the hex number B to decimal.

11*16^0=11

Answer: 11

Q15: If reading the byte 0x21 as a number, what decimal number would it mean?

2*16^1 + 1*16^0

Answer: 33

Q16: Continues in Part-2
