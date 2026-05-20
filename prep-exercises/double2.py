def double(number):
    return number * 3

print(double(10))

# The but in this code is that the parameter type of the variable number is not
# specified, the function takes whatever passed and multiplies it by 3, so if we 
# pass a string it will concatenate the string 3 times instead of multiplying the number by 3.