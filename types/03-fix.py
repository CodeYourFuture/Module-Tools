def double(number):
    return number * 3

print(double(10))

# TASK 3:
# Read the code and see if you can find any bugs.
# Write down what the bug is, and how would you fix it?
# Are there multiple ways you could fix it?

# The intention from the name is to double, where we are tripling
# The inverse could also be true.

# The following are valid fixes:

def triple(number):
    return number * 3

def double(number):
    return number * 2