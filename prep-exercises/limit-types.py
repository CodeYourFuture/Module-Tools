def double(number):
    return number * 3

print(double(10))

# The bug is that method naming(double), as this method is multiplying the number by 3, should be named triple, to make sense of the method scope,
# and show other developers what is the purpose of it even before reading the code.
# Or we can change the multiplied by number from 3 to 2 to match the correct meaning of the method.
