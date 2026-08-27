def double(number):
    return number * 3


print(double(10))

# our function is supposed to double the input value, but the function return triple.
# to fix this we have two options:


# First: we can change the name of function from double to triple.
def triple(number):
    return number * 3


print(triple(10))


# Second: we should multiply the input by 2.
def double(number):
    return number * 2


print(double(10))
