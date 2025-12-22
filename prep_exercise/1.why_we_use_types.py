# exercise
# Predict what double("22") will do. Then run the code and check. Did it do what you expected? Why did it return the value it did?

def half(value):
    return value / 2

def double(value):
    return value * 2

def second(value):
    return value[1]

print(double("22"))

# My prediction was that double("22") would print 44.
# After running the code, I realized it prints "2222" because
# multiplying a string by an integer in Python repeats the string.
#
# What I have learned is that in Python, the * operator behaves
# differently depending on the data type. For example:
# - with integers, it performs mathematical multiplication
# - with strings, it performs string repetition
