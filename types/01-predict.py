def half(value):
    return value / 2

def double(value):
    return value * 2

def second(value):
    return value[1]

# TASK 1:
# 1. Predict what you think will happen with each of the following functions
# 2. Then, test it, and explain in your own words what is actually happening and why
# (feel free to comment out lines if you think they cause errors or crashes while testing)

print(half(22))
# Prediction:
# What actually happens and why: 11.0, the int gets turned into a float by division

# print(half("22"))
# Prediction:
# What actually happens and why: Error, "halving" is undefined for strings

print(double(22))
# Prediction:
# What actually happens and why: 44, multiplication of ints

print(double("22"))
# Prediction:
# What actually happens and why: "2222", multiplication is overloaded in python and repeats strings

# print(second(22))
# Prediction:
# What actually happens and why: you cannot index / subscript through an integer

# print(second(0x16))
# Prediction:
# What actually happens and why: 0x16 is an integer defined in a different base, the 'x' isn't a string value

print(second("22"))
# Prediction:
# What actually happens and why: "2", this is a string, and we are getting the second character
