# Question

def double(number):
    return number * 3

print(double(10))

# Read the above code and write down what the bug is. How would you fix it?


# Answer
# The bug: The function multiplies the number by 3 instead of 2, which contradicts its name.

# Proposed fix: We can either change the function implementation so that it returns number * 2 or we change the function name to 'triple'