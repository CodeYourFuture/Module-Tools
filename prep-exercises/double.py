def double(value):
    return value * 2

# Prediction - Since a string was passed as parameter, it will concatenate twice rather than multiply the number.

print(double("22"))

def double_number(value):
    return value * 3 
# The bug is multiplying by 3 rather than 2 as the function name implies. 
# To fix this, simply return value * 2

print(double_number(10))
