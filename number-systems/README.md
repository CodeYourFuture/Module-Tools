Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

Convert the decimal number 14 to binary.
Answer: **1110**

Convert the binary number 101101 to decimal:
    Answer: 32+8+4+1 = **45**
                AND
            It can be **-19** as well, 010011 => 16+2+1 = 19 but negative

Which is larger: 1000 or 0111?
    Answer: If consider as **UNsigned** binary: **1000** as 8 > 7 
                OR
            If consider as **Signed** binary: **0111** as 7 > -8 0111 + 1 = 1000 => -8

Which is larger: 00100 or 01011?
    Answer: **01011**

What is 10101 + 01010?
    Answer: **11111**

What is 10001 + 10001?
    Answer: **100010**

What's the largest number you can store with 4 bits, if you want to be able to represent the number 0?
    Answer: **15**

How many bits would you need in order to store the numbers between 0 and 255 inclusive?
    Answer: **8 bits**

How many bits would you need in order to store the numbers between 0 and 3 inclusive?
    Answer: **2 bits**

How many bits would you need in order to store the numbers between 0 and 1000 inclusive?
    Answer: `2^n - 1` => 2^10 - 1 = 1023 => **10 bits**

How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
    Answer: I can check if the binary number include **ONLY one "1"**, it`s a power of two, since each bit represent a power two.
            **But I don`t know what you mean by the word "test" here**

Convert the decimal number 14 to hex.
    Answer: **E**

Convert the decimal number 386 to hex.
    Answer: 386/16 = 24 and 2 remainder
            24/16  = 1  and 8 remainder
            1/16 = 0    and 1 remainder
            So **182**

Convert the hex number 386 to decimal.
    Answer: 16^2 * 3 = 768
            16^1 * 8 = 128 
            16^0 * 6 = 6
            So **902**

Convert the hex number B to decimal.
    Answer: **11**

If reading the byte 0x21 as a number, what decimal number would it mean?
    Answer: **33**

If reading the byte 0x21 as an ASCII character, what character would it mean?
    Answer: According to `ASCII table` it`s **!**

If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
    Answer: Since greyscale colour range can be from `0 (black) to 255 (white)`, and `0x21 = 0d33`, So it means **Very Dark Gray close to Black**

If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
    Answer: Since we got `AA = 170 Red`, `00 = no Green`, `FF = 255 Blue`, it representing **Dark Blue close to Purple**

If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
    Answer: 1st byte `AA` = **170**
            2nd byte `00` = **0**
            3rd byte `FF` = **255**