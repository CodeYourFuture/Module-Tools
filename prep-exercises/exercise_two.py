def double(number):
    return number * 3

print(double(10))

# Read the above code and write down what the bug is. How would you fix it?

# the bug here is logical: the function name: "double" - which contradicts what it does. 
# Named double but it triples the parameter passed.
# To fix it either do:

# A:
def double(number):
    return number * 2

print(double(10))


# or B:
def triple(number):
    return number * 3

print(triple(10))



