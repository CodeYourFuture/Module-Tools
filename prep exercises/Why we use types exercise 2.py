def double(number):
    return number * 3

print(double(10))

# There are two possible ways to fix the bug.

# 1. The function name is wrong, it needs to be named to triple
# 2. Or the function name is correct but the calculation is wrong, it should be return * 2

def double(number):
    return number * 2

value = 10
print(double(value))
