Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

Convert the decimal number 14 to binary.
Answer: 1110
```
14 : 2 = 7 R 0
7 : 2 = 3 R 1
3 : 2 = 1 R 1
1 : 2 = 0 R 1
==> 1110 
```

Convert the binary number 101101 to decimal:
Answer:

```
32 + 0 + 8 + 4 + 0 + 1 = 45
```


Which is larger: 1000 or 0111?
Answer: 1000

Which is larger: 00100 or 01011?
Answer: 01011

What is 10101 + 01010?
Answer: 11111
```
 10101
 01010
 -----
 11111
```

What is ?
Answer:
```
   1   1
    10001
    10001
    -----
   100010
```

What's the largest number you can store with 4 bits, if you want to be able to represent the number 0?
Answer: 16 
```
 2 pow 4 
 ```

How many bits would you need in order to store the numbers between 0 and 255 inclusive?
Answer: 8
```
2 pow 8 = 256
```

How many bits would you need in order to store the numbers between 0 and 3 inclusive?
Answer: 2
```
2 pow 2 = 4
```

How many bits would you need in order to store the numbers between 0 and 1000 inclusive?
Answer: 10
```
2 pow 9 = 512
2 pow 10 = 1024
```

How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
Answer: 
```
power of two => 10000....0
minus 1 => 01111.....1
after multiplying => 0
```

Convert the decimal number 14 to hex.
Answer: 14

Convert the decimal number 386 to hex.
Answer: 182
```
386 : 16 = 24 R 2
24 : 16 = 1 R 8
1 : 16 = 0 R 1
------------
182
```

Convert the hex number 386 to decimal.
Answer: 902
```
256 * 3 + 16 * 8 + 1 * 6  = 902
```

Convert the hex number B to decimal.
Answer: 11

If reading the byte 0x21 as a number, what decimal number would it mean?
Answer: 33

If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer: !

If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: gray
```
from 0 where it is black 
to 255 where it is white
33 => gray
```

If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: pinkish purple
```
AA => 170 of red
00 => 0 of green
FF => 255 of blue
```

If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
Answer: 170 0 255