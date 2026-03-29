# ================= exercise ===============================
# Read the code and write down what the bug is. How would you fix it?

def double(number):
    return number * 3

print(double(10))

# The bug in the code is that the function is named double(), but it multiplies
# the number by 3 instead of 2. This makes the function behavior inconsistent
# with its name.

# To fix this, either:
# - we need to change the function to return number * 2, or
# - rename the function to triple() if multiplying by 3 is the intended behavior.
